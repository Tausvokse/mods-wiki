<script setup>
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import models from '../data/unicrates-models.json'
const search = ref('')
const visible = computed(() => models.filter(row => `${row.id} ${row.name}`.toLowerCase().includes(search.value.trim().toLowerCase())))
</script>

<template>
  <section class="uc-gallery" aria-label="Built-in crate model gallery">
    <div class="uc-gallery-filters"><label>Find a model<input v-model="search" type="search" placeholder="Name or model ID…" /></label></div>
    <p class="uc-gallery-count" role="status">{{ visible.length }} of {{ models.length }} models · Closed crates photographed in Minecraft.</p>
    <div class="uc-gallery-grid">
      <article v-for="model in visible" :key="model.id" class="uc-preview">
        <img :src="withBase(model.image)" :alt="`${model.name} closed crate in Minecraft`" width="480" height="270" loading="lazy" decoding="async" />
        <div class="uc-preview-caption">
          <strong>{{ model.name }}</strong><code>{{ model.id }}</code>
          <span>Matching key custom model data: {{ model.keyCustomModelData }}</span>
          <a :href="withBase(`/unicrates/custom-content/gallery?opening=${model.previewOpening}`)">Watch a recorded opening using this model</a>
        </div>
      </article>
    </div>
  </section>
</template>
