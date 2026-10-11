<script setup>
import { computed, onMounted, ref } from 'vue'
import previews from '../data/unicrates-previews.json'

const search = ref('')
const category = ref('All openings')
const playing = ref('')
const categories = ['All openings', ...new Set(previews.map(row => row.category))]
const visible = computed(() => {
  const query = search.value.trim().toLowerCase()
  return previews.filter(row => (category.value === 'All openings' || row.category === category.value)
    && `${row.id} ${row.name} ${row.category}`.toLowerCase().includes(query))
})
onMounted(() => {
  const opening = new URLSearchParams(window.location.search).get('opening')
  if (opening && previews.some(row => row.id === opening)) search.value = opening
})
</script>

<template>
  <section class="uc-gallery" aria-label="Recorded opening animation gallery">
    <div class="uc-gallery-filters">
      <label>Find an opening<input v-model="search" type="search" placeholder="Name, ID or category…" /></label>
      <label>Category<select v-model="category"><option v-for="name in categories" :key="name">{{ name }}</option></select></label>
    </div>
    <p class="uc-gallery-count" role="status">{{ visible.length }} of {{ previews.length }} openings · Click a preview to play. Only one GIF plays at a time.</p>
    <div class="uc-gallery-grid">
      <AnimationPreview v-for="entry in visible" :key="entry.id" :id="entry.id" v-model="playing" />
    </div>
    <p v-if="!visible.length">No matching openings. Try a shorter name or choose All openings.</p>
  </section>
</template>
