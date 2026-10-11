# Storage, backups and recovery

UniCrates stores crate definitions separately from player state. Changing reward JSON does not reset opening counts, virtual keys, daily limits, pending transactions or global win counters.

## What must be preserved

| Data | Location / owner |
| --- | --- |
| Crates, timelines, resources, global settings and language | `config/unicrates/` |
| Flatfile player records | `config/unicrates/data/players/<uuid>.json` |
| SQL player records | Selected SQLite/MySQL data store; JDBC persists player snapshots |
| Global reward wins, reservations, completed reservation evidence | `config/unicrates/data/global_limits.json`, even with SQL player backend |
| SQL destination migration marker | `config/unicrates/data/.migrated_to_jdbc` |
| Migration source backups | `config/unicrates/data/backup_flatfile_*` |
| Configuration snapshots | `config/unicrates/.backups/backup_*` |
| Player inventories, crate block entities/display entities | Minecraft world/player data |
| Pokémon party/PC | Cobblemon storage |
| Economy and permission provider state | Impactor/economy and LuckPerms persistence |
| Win log | `logs/unicrates/rewards.log`; diagnostic log, not a balance database |

Player records include virtualKeys, cooldowns, pityCounters, totalCrateOpens, lifetimeRewardWins, dailyLimits, milestone claims, opening history, pending rewards/payment/command intent, prepared Pokémon/external rewards and completion/settlement evidence. These fields form a transaction record; editing one field alone can make the remainder inconsistent.

Global limits remain local file-backed state. Selecting MySQL does **not** turn several independent servers into a coordinated shared crate network. Coordinate world and external-provider ownership yourself before considering multi-server deployments.

## Choosing a backend

`storage.backend` is read when the server constructs `UniCrates`. Restart to switch destinations. SQL loading/saving is dispatched through the player transaction coordinator rather than doing blocking JDBC work directly in ordinary server-thread reward paths.

### Flatfile

Default:

```json
{
  "storage": { "backend": "flatfile" }
}
```

One UUID JSON file per player. A migrated-to-SQL marker prevents switching back to obsolete JSON snapshots by simply changing backend. Storage read failures must be repaired from evidence/backups; do not replace a failed record with an empty object to silence the error.

### SQLite

```json
{
  "storage": {
    "backend": "sqlite",
    "sqlite": { "file": "data/unicrates.db" }
  }
}
```

This resolves to `config/unicrates/data/unicrates.db`. An absolute path is supported; ensure its parent directory exists and is writable. For portable backups, stop the server cleanly before copying the database. If capturing a live database, use a database-aware snapshot that also accounts for journal/WAL state rather than copying only the main file during writes.

### MySQL / MariaDB

```json
{
  "storage": {
    "backend": "mysql",
    "mysql": {
      "host": "127.0.0.1",
      "port": 3306,
      "database": "unicrates",
      "user": "unicrates",
      "password": "REPLACE_WITH_YOUR_DATABASE_PASSWORD",
      "useSsl": false
    }
  }
}
```

Create the database/user and make the endpoint reachable before restart. The store creates its table in the selected database; it does not provision the database server or database account. `mariadb` chooses the same MySQL JDBC implementation. `useSsl` is passed as the JDBC useSSL option; do not infer certificate verification or a complete TLS policy from this one boolean.

If the destination cannot initialize or its identity conflicts with the marker, startup fails rather than silently selecting flatfile. Preserve the error and fix destination/authentication/marker consistency.

## Automatic flatfile-to-SQL migration

On startup with SQLite/MySQL, the migration reads existing UUID files in `data/players/`. Before target writes it copies and verifies source files into a timestamped `backup_flatfile_*` directory. It loads and saves each record, then writes `.migrated_to_jdbc` containing the destination identity. A failed source backup stops migration before writes. Invalid non-UUID filenames are skipped with a warning.

The marker suppresses repeated migration and binds the source snapshot to the selected destination. A marker belonging to another database stops startup; a legacy marker with no identity requires an existing nonempty destination before it can be bound. Keep migration backups and the marker.

There is **no built-in reverse export or SQL-to-SQL migration command**. To change SQLite paths, move to another MySQL database, or return to flatfile, first export current SQL records with tooling that preserves their complete player snapshots and transaction identities. Do not remove the marker and import old player JSON: those files can contain stale balances and incomplete transaction evidence.

Recommended sequence:

1. Prevent new openings and stop the server cleanly.
2. Back up `config/unicrates/`, world/player data, Cobblemon data and external provider stores at a consistent point.
3. Configure the SQL destination; restart in a maintenance/test environment.
4. Read migration/startup logs and compare player records, virtual keys, pending states and counters against the source backup.
5. Resume play only after the active destination and marker agree.

## Configuration backup and manual restoration

Web editor apply creates snapshots of `crates/`, `animations/` and `resources/`, retaining the latest **10** snapshots. These are configuration backups, not full server backups. Manual reload does not create this snapshot automatically.

There is an internal `restoreFromBackup` API but no public rollback command. For an owner-managed restoration, stop the server, preserve the current directories, and copy the desired snapshot's crate/timeline/resources directories back as a consistent set. Restart and inspect load errors. Restore `main-config.json` or `discord.yml` only from your own backups; the editor snapshots do not cover them.

Do not delete `.staging`, `.swap_backup` or configuration transaction journal files merely because they look temporary while a server is running. Startup recovery uses these artifacts to restore coherent configuration after interruptions.

## Pending transactions and administrator recovery

Before payment/reward effects, the opening pipeline persists intent and reserves global slots. Login recovery attempts pending delivery when its dependencies and original crate/reward definitions are available. A missing crate/reward produces an unavailable-reward message: restore its definition and integration rather than deleting the pending entry.

Prepared Pokémon records freeze the exact Pokémon identity/data and reconcile actual party/PC slots. Commands have an outbox and saved success acknowledgements. External economy deposits and opening withdrawals have checkpoints. These mechanisms reduce duplicate effects but do not make every external action exactly-once: commands or deposits may have happened before a crash prevented acknowledgement. Physical inventory and other mods' data saves are also separate persistence boundaries.

When a payment outcome is uncertain, the code stops automatic repeat of payment/reward and asks for administrator review. An economy deposit left REQUESTED is also held for review. Establish the actual external balance/effect before compensating; a reconnect is not evidence that nothing was delivered.

### Review first

```text
/crate pending status Alex
```

The target must be online. Record the transaction ID, current fingerprint and full detail output. It includes diagnostic identities, prepared reward/payment/command state and settlement evidence. Keep the player still; movement, config edits and state changes can invalidate review. Re-run status after any such change.

A normal dependency repair may be enough: restore the original crate/reward ID or missing provider and let next-login recovery continue. Current frozen command batches retain original resolved commands; editing JSON does not replace those batches.

### Adopt commands for a legacy pending opening

```text
/crate pending adopt-current Alex <transaction_id> <current_fingerprint> accept-replay-risk
```

Only use this after reviewing a legacy pending opening that lacks its original frozen command snapshot. This explicitly accepts current replacement commands and possible replay. It persists command snapshots without immediate payout or refund; normal recovery runs at the player's next login. It is not a generic fix for uncertain economy effects.

### Settle without issue or refund

```text
/crate pending mark-settled Alex <new_operation_uuid> <current_fingerprint> no-issue-no-refund
```

Choose a new UUID as the operation identity. This closes the **whole reviewed pending opening** without granting its reward or returning payment. Known reservation cleanup and durable settlement receipt are recorded. Unknown or conflicting identities remain diagnostic evidence. Preserve operation UUID and fingerprint for an exact retry if interrupted; do not invent a different operation merely to bypass a conflict.

Any manual replacement reward or refund is a separate administrator decision based on the reviewed provider/world state. Record it independently. There is no automatic issue/refund option on mark-settled.

## Routine operational checks

Use `/crate stats <player> [crate]`, key balance and pending status to inspect records. Keep IDs stable during live content changes. Back up global_limits.json together with the selected player store and world/provider stores. Do not reset reward counters by deleting files while pending reservations exist. For symptom-based checks, see [troubleshooting](../getting-started/troubleshooting).

Source: `UniCrates.createDataStore`, `DataMigration`, `FlatFilePlayerDataStore`, `JdbcPlayerDataStore`, `PlayerData`, `PlayerTransactionCoordinator`, `GlobalLimitStore`, `ConfigManager`, `ConfigSnapshotTransaction`, `RewardDelivery`, `PendingCommandRecovery`, `PendingSettlementRecovery`, `EconomyPaymentCheckpoint`.
