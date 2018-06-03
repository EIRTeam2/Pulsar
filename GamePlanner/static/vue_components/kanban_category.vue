<template>
  <div class="column scolumn">
    <p class="kanban-title">{{category.display_name}}</p>
    <vddl-list :inserted="on_inserted" class="column scolumn" :list="category.nodes" :horizontal="false">
      <vddl-draggable v-for="(node, node_index) in category.nodes" v-if="node.stage==category.name && node.milestone.id==milestone.id" :wrapper="category.nodes" :index="node_index" :draggable="node">
        <Task :task="node"></Task>
      </vddl-draggable>
      <vddl-placeholder class="red is-size-7">Drop to add as children</vddl-placeholder>
    </vddl-list>
  </div>
</template>
<script>
import {getCookie} from 'scripts/csrf.js';

var rest = require('rest');

var csrf = require('rest/interceptor/csrf')
var mime = require('rest/interceptor/mime')
var client = rest.wrap(csrf, {name: "X-CSRFToken" ,token: getCookie("csrftoken") })
client = client.wrap(mime)
import Task from 'vue_components/task.vue';

module.exports = {
  name:"KanbanBoard",
  props: {
    category: {
      required: true
    },
    milestone: {
      required: true
    }
  },
  components: {
    "Task": Task
  },
  data: function() {
    return {
    }
  },
  methods: {
    on_inserted : function(result) {
      result.item.stage = this.category.name
      var resulting_entity = {
        id: result.item.id,
        stage: this.category.name
      }
      client({
        path: "/api/task/" + result.item.id + "/",
        method: "PATCH",
        headers: {
          'Content-Type': 'application/json'
        },
        entity: resulting_entity
      }).then(function(response) {
        console.log('response', response)
      })
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
