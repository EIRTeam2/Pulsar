<template>

<div class="columns scolumns">
  <KanbanCategory v-for="(category, cat_index) in categories" :category="category" :milestone="milestone"></KanbanCategory>
</div>
</template>

<script>
import {getCookie} from 'scripts/csrf.js';
import KanbanCategory from 'vue_components/kanban_category.vue';

var rest = require('rest');

var csrf = require('rest/interceptor/csrf')
var mime = require('rest/interceptor/mime')
var client = rest.wrap(csrf, {name: "X-CSRFToken" ,token: getCookie("csrftoken") })
client = client.wrap(mime)
module.exports = {
  name:"kanban",
  components: {
      "KanbanCategory": KanbanCategory
  },
  props: {
    categories: {
      required: true
    },
    milestone: {
      required: true
    }
  }
}
</script>

<style>
.scolumns {
    flex-wrap: wrap;
    align-items: stretch;
}

.scolumn {
  min-height: 300px;
}

.box {
  margin: 0;
  margin-top: 0.25rem;
}

.box:not(:last-child) {
  margin: 0;
  margin-top: 0.25rem;
}


.item-box {
  border-radius: 0;
  left: 10px;
  margin-bottom: 0;
  box-shadow: none;
  border: none;
  background-color: #FFF;
}
.kanban-title {
  background-color: grey;
  color: white;
  padding: 0.50rem;
}

.vddl-list {
  min-height: 100px;
}

.vddl-draggable {
  margin: 0;
  cursor: move;
}

.item-box {
  border-radius: 0;
  left: 10px;
  margin-bottom: 0;
  box-shadow: none;
  border: none;
  background-color: #FFF;
}

</style>
