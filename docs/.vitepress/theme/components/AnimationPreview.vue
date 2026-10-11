<script setup>
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import previews from '../data/unicrates-previews.json'

const props = defineProps({ id: String, modelValue: String })
const emit = defineEmits(['update:modelValue'])
const localPlaying = ref(false)
const entry = computed(() => previews.find(row => row.id === props.id))
const playing = computed(() => props.modelValue === undefined ? localPlaying.value : props.modelValue === props.id)
function toggle() {
  if (props.modelValue === undefined) localPlaying.value = !localPlaying.value
  else emit('update:modelValue', playing.value ? '' : props.id)
}
</script>

<template>
  <article v-if="entry" class="uc-preview">
    <button class="uc-preview-screen" type="button" :aria-label="`${playing ? 'Stop' : 'Play'} GIF: ${entry.name}`" :aria-pressed="playing" @click="toggle">
      <img :src="withBase(playing ? entry.gif : entry.poster)" :alt="`${entry.name} — recorded Minecraft opening`" width="480" height="270" loading="lazy" decoding="async" />
      <span class="uc-preview-control">{{ playing ? 'Stop GIF' : '▶ Play GIF' }}</span>
    </button>
    <div class="uc-preview-caption">
      <strong>{{ entry.name }}</strong>
      <code>{{ entry.id }}</code>
      <span>{{ entry.category }} · Recorded {{ entry.recordedOn }}</span>
      <a :href="withBase(entry.gif)" target="_blank" rel="noopener">Open GIF</a>
    </div>
  </article>
</template>
