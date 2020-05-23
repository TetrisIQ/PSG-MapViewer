<template>
  <div id="app">
    <Overlayer/>
    <Map/>
    <input id="demo"/>
    <button @click="demo">TEST</button>
  </div>
</template>

<script>
import Map from './components/Map.vue';
import Overlayer from './components/Overlayer.vue';

export default {
  name: 'App',
  components: {
    Map,
    Overlayer
  },
  methods: {
    demo() {
      this.$store.commit("msg", document.getElementById("demo").value)
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 1em;
}
</style>
