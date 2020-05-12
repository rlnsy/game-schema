<template>
  <div id="app">
      <div class="welcome">
      <img
        src="@/assets/game.png"
        alt="game splash"
      ><br>
      <h1>{{ name }} v{{ version }}</h1>
      </div>
  </div>
</template>

<style lang="scss" scoped>
.welcome{
    height: 100%;
    width: 100%;
    margin-top: 15vh;
    display:flex;
    flex-direction: column;
    align-content: center;
    align-items: center;
    font-size: 22px;
    > img {
        height: 300px;
        width: auto;
        padding: 20px;
    }
}
</style>


<script>

import {getInfo} from './utils/info.js'

export default {
  name: 'App',
  components: {},
  data() {
    return {
      appUrl: "LOADING",
      name: "LOADING",
      version: "LOADING"
    }
  },
  async mounted(){
    this.appUrl = process.env.APP_URL;
    let infoResponse = await getInfo();
    this.name = infoResponse.data['name'];
    this.version = infoResponse.data['version'];
  },
  methods: {},
};
</script>

<style lang="scss">
$primary: #828EFF;
@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';


body{
  margin: 0;
  padding: 0;
}

h1, h2, h3, h4 {
  font-family: 'Roboto', sans-serif;
  font-weight: 600 !important;
  margin: 0 !important;
}

#app {
  text-shadow: 1px 1px 1px rgba(0,0,0,0.004);
  text-rendering: optimizeLegibility !important;
  -webkit-font-smoothing: antialiased !important;
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100vh;
  width: 100vw;
  display: flex;
  overflow: hidden;
}

</style>
