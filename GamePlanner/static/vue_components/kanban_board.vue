<template>
  <div class="column scolumn">
    <p class="kanban-title">{{category.display_name}}</p>
    <vddl-list :inserted="on_inserted" class="column scolumn" :list="category.nodes" :horizontal="false">
      <vddl-draggable v-for="(node, node_index) in category.nodes" v-if="node.fields.stage==category.name" class="box item-box" :wrapper="category.nodes" :index="node_index" :draggable="node">
        <p><strong>#{{node.pk}} </strong>{{node.fields.title}}</p>
        <p></p>
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

module.exports = {
  name:"KanbanBoard",
  props: {
    category: {
      required: true
    }
  },
  data: function() {
    return {
    }
  },
  methods: {
    on_inserted : function(result) {
      result.item.fields.stage = this.category.name
      var resulting_entity = {
        id: result.item.pk,
        stage: this.category.name
      }
      client({
        path: "/api/task/" + result.item.pk + "/",
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
