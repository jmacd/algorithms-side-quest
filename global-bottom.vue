<script setup>
import { computed } from 'vue'
import { useNav, useSlideContext } from '@slidev/client'

const nav = useNav()
const ctx = useSlideContext()

const section = computed(() => ctx?.$frontmatter?.section ?? '')
const page = computed(() => nav.currentPage.value ?? 0)
const total = computed(() => nav.total.value ?? 0)
</script>

<template>
  <div class="footer">
    <div class="footer-left">{{ section }}</div>
    <div class="footer-right">{{ page }} / {{ total }}</div>
  </div>
</template>

<style scoped>
.footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 1.2rem;
  font-size: 0.75rem;
  color: #777;
  pointer-events: none;
  font-family: 'Roboto', system-ui, sans-serif;
}
.footer-right {
  font-family: 'Roboto Mono', ui-monospace, monospace;
}
</style>
