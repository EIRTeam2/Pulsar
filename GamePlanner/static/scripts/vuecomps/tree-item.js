import Vddl from 'vddl';
import Vue from "vue";
Vue.component('tree-item', {
data: function () {
  return {

  }
},
props: ["node", "nodes", "index", "callback"],
delimiters: ["[[","]]"],
template: '<vddl-draggable :selected="callback" class="panel__body--item" :key="node.id" :draggable="node" :index="index" :wrapper="nodes" effect-allowed="move"> <details class="box"> <summary> List [[node.name]] </summary> <vddl-list :list="node.children" :horizontal="false"> <tree-item v-for="(child, c_index) in node.children" :callback="callback" :index="c_index" :nodes="node.children" :key="child.id" :node="child"> </tree-item> <vddl-placeholder class="red">Custom placeholder</vddl-placeholder> </vddl-list> </details> </vddl-draggable>',
});
