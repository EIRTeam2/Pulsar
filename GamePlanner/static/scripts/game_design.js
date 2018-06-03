import Vddl from 'vddl';
import Vue from "vue";
import VueMarkdown from 'vue-markdown';
import treeitem from 'vue_components/tree-item.vue';
import EditableInput from 'vue_components/editable-input.vue';
import markdownEditor from 'vue_components/markdown_editor.vue';
import tab from 'vue_components/tab.vue';
import tabs from 'vue_components/tabs.vue';
import vClickOutside from 'v-click-outside'
import {getCookie, ajaxOption} from 'scripts/csrf.js';
import Task from 'vue_components/task.vue';

var rest = require('rest');

var csrf = require('rest/interceptor/csrf')
var mime = require('rest/interceptor/mime')
var client = rest.wrap(csrf, {name: "X-CSRFToken" ,token: getCookie("csrftoken") })
client = client.wrap(mime)

console.log(getCookie("csrftoken"))



function getNodeById(id, node){
    var reduce = [].reduce;
    function runner(result, node){
        if(result || !node) return result;
        return node.id === id && node || //is this the proper node?
            runner(null, node.children) || //process this nodes children
            reduce.call(Object(node), runner, result);  //maybe this is some ArrayLike Structure
    }
    return runner(null, node);
}

Vue.use(Vddl);
Vue.use(VueMarkdown);

Vue.config.debug = true;



var app = new Vue({
  el: '#design-editor-app',
  delimiters: ["[[","]]"],
  components: {
    treeitem: treeitem,
    editableinput: EditableInput,
    tab: tab,
    tabs: tabs,
    task: Task,
    VueMarkdown
  },
  methods: {
    item_selected : function(event) {
      this.select_node(event.id)
    },
    select_node : function(node_id) {
      console.log("UWU")
      this.viewing_node = true
      this.editing_object = getNodeById(node_id, this.nodes)
      console.log(this.editing_object)
    },
    on_inserted : function(result) {
      // removes all parents from dropped child

      var resulting_entity = {
            id: result.item.id,
            parent: null
      }
      client({
        path: "/api/design_element/" + result.item.id + "/",
        method: "PATCH",
        headers: {
          'Content-Type': 'application/json'
        },
        entity: resulting_entity
      }).then(function(response) {
          console.log('response: ', response);
      });

    }
  },
  data: {
    editing_object: {id: -1},
    property_list: [{
      "display_name": "Name",
      "field": "name",
      "editor": "text"
    }],
    "nodes": "",
    "project": {},
    "resource_type": "design_element",
    "viewing_node": false,
    "lists": {
      "A": [
        {
          "id": 1,
          "label": "Item A1"
        },
        {
          "id": 2,
          "label": "Item A2"
        },
      ]
      }
  },
})


window.set_nodes = function (nodes) {
  app.nodes = nodes
}

window.set_project = function (project) {
  console.log(project)
  app.project = project
}
