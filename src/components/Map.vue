<template>
  <div class="map">
    <div v-for="row in fieldData.rows" v-bind:key="row.id" class="row">
      <div v-for="col in row.fields" v-bind:key="col.id" class="col">
        <div class="field">
          <div v-if="col.meeple !== undefined">
            <Field :data="col.meeple" :coordinate="col.coordinate" />
          </div>
          <div v-else>
            <Field :coordinate="col.coordinate"/>
            <!-- {{col.coordinate.xCoordinate}}/{{col.coordinate.yCoordinate}} -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Field from "./Field.vue";
import { RepositoryFactory } from "./../repository/RepositoryFactory";
const AdminRepo = RepositoryFactory.get("admin");

export default {
  name: "Map",
  components: {
    Field
  },
  data() {
    return {
      fieldData: [],
      timer: {}
    };
  },
  methods: {
    async fetchMap() {
      const { data } = await AdminRepo.getMap();
      this.fieldData = data;
      console.log("Map Updated");
      console.log(data)
    }
  },
  created() {
    ////this.timer = setInterval(this.fetchMap, 200);
    this.fetchMap();
  }
};
</script>

<style lang="scss" scoped>
.row {
  margin: 0px;
}

.map {
  margin-right: 2em;
  margin-left: 2em;
}

.col {
  margin: 0px;
  padding: 0px;
}

.field {
  background-color: gray;
  border-style: solid;
  border-color: black;
  border-width: 1px;
}
</style>