<template>
  <div id="overlayer" class="hidden">
    <h1>{{msg}}</h1>
    {{update}}
  </div>
</template>

<script>
export default {
  name: "overlayer",
  data() {
    return {
      oldMsg: this.$store.getters.msg
    };
  },
  methods: {
    disapear() {
      document.getElementById("overlayer").classList.add("hidden");
    },
    show() {
      setTimeout(this.disapear, 1500);

      document.getElementById("overlayer").classList.remove("hidden");
    }
  },
  computed: {
    msg() {
      return this.$store.getters.msg;
    },
    update() {
      if (this.msg != this.oldMsg) {
        console.log("Update");
        this.show();
        this.oldMsg = this.msg;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.hidden {
  display: none;
}

h1 {
  padding: 50px 0;
  text-align: center;
}

#overlayer {
  position: fixed;
  top: 20vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 2;
  width: 100%;
  height: 20vh;
  color: white;
}
</style>