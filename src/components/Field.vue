<template>
  <div>
    <div v-if="this.data == undefined">
      <img
        src="./../assets/empty_sky.svg"
        data-toggle="tooltip"
        v-bind:title="'[' + this.coordinate.xcoordinate + '/' + this.coordinate.ycoordinate + ']'"
      />
    </div>
    <div v-else>
      <div v-if="this.data.name == 'SpaceStation'">
        <SpaceStation
          :color="this.data.color"
          :tooltip="'[' + this.coordinate.xcoordinate + '/' + this.coordinate.ycoordinate + '] ' + this.data.username + ' Space Station'"
        />
      </div>
      <div v-if="this.data.name == 'Starfighter'">
        <Starfighter
          :color="this.data.color"
          :tooltip="'[' + this.coordinate.xcoordinate + '/' + this.coordinate.ycoordinate+ '] ' + this.data.username + ' Starfighter'"
        />
      </div>
      <div v-if="this.data.name == 'Transporter'">
        <Transporter
          :color="this.data.color"
          :tooltip="'[' + this.coordinate.xcoordinate + '/' + this.coordinate.ycoordinate+ '] ' + this.data.username + ' Transporter'"
        />
      </div>
    </div>
  </div>
</template>

<script>
import SpaceStation from "./Meeple/SpaceStation";
import Starfighter from "./Meeple/Starfighter";
import Transporter from "./Meeple/Transporter";

export default {
  name: "field",
  props: ["data", "coordinate"],
  components: { SpaceStation, Starfighter, Transporter },
  methods: {
    createHoverText() {
      return (
        this.data.coordinate.xCoordinate + "/" + data.coordinate.yCoordinate
      );
    }
  }
};
</script>

<style lang="scss" scoped>
</style>