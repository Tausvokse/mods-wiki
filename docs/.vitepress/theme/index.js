import DefaultTheme from 'vitepress/theme'
import AnimationPreview from './components/AnimationPreview.vue'
import UniCratesGallery from './components/UniCratesGallery.vue'
import ModelGallery from './components/ModelGallery.vue'
import './unicrates.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('AnimationPreview', AnimationPreview)
    app.component('UniCratesGallery', UniCratesGallery)
    app.component('ModelGallery', ModelGallery)
  }
}
