(this.webpackJsonpclient_example=this.webpackJsonpclient_example||[]).push([[0],{43:function(e,t,a){},44:function(e,t,a){e.exports=a.p+"static/media/create-white-36dp.5014967b.svg"},45:function(e,t,a){e.exports=a.p+"static/media/remove-white-36dp.9574eed3.svg"},57:function(e,t,a){e.exports=a(70)},62:function(e,t,a){},63:function(e,t,a){},64:function(e,t,a){},65:function(e,t,a){},66:function(e,t,a){},70:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),o=a(10),i=a.n(o),s=(a(62),a(105)),c=a(48),d=a(12),l=a(13),h=a(11),p=a(15),m=a(14),u=(a(63),a(31)),v=(a(64),a(49)),f=(a(43),function(e){Object(p.a)(a,e);var t=Object(m.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){var e=Object(v.a)({},this.props);delete e.transform,delete e.name,delete e.key;var t={};if(this.props.transform){var a=this.props.transform,n=a.x?a.x:0,o=a.y?a.y:0;t.transform="translate(".concat(n,"px,").concat(o,"px)")}return r.a.createElement("div",{className:"node",style:t},r.a.createElement("div",Object.assign({className:"node-item"},e,{style:{backgroundColor:this.props.color?this.props.color:"white"}}),r.a.createElement("p",null,this.props.name)))}}]),a}(r.a.Component)),b=(a(65),Math.sqrt(2)),y=function(e){Object(p.a)(a,e);var t=Object(m.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){var e={opacity:this.props.opacity?this.props.opacity:1};if(this.props.transform){var t=this.props.transform,a=t.x?t.x:0,n=t.y?t.y:0,o=this.props.transform.rotate,i=o%2!==0?b:1;e.transform="translate(".concat(a+20,"px,").concat(n+20,"px) rotate(").concat(45*o,"deg) scaleX(").concat(i,")")}return r.a.createElement("hr",{className:"edge",style:e})}}]),a}(r.a.Component),E=function(e){Object(p.a)(a,e);var t=Object(m.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this,e)).drawNodes=n.drawNodes.bind(Object(h.a)(n)),n.drawEdges=n.drawEdges.bind(Object(h.a)(n)),n.setNode=n.setNode.bind(Object(h.a)(n)),n.state={},n}return Object(l.a)(a,[{key:"setNode",value:function(e){if(this.props.data&&this.props.data.nodes){var t=this.props.data.nodes[e];if(t){var a,n={},r=Object(u.a)(t.children);try{for(r.s();!(a=r.n()).done;){n[a.value]=!0}}catch(o){r.e(o)}finally{r.f()}this.setState({activeNode:e,targets:n})}}}},{key:"drawNodes",value:function(){var e=this,t=[];if(this.props.data&&this.props.data.nodes){var a=this.props.data.nodes,n=function(n){if(a.hasOwnProperty(n)){var o=a[n],i="white";e.state.activeNode===n?i="rgb(97, 205, 187)":e.state.targets&&e.state.targets[n]&&(i="rgb(244,117,96)"),t.push(r.a.createElement(f,{key:n,color:i,name:n,onMouseEnter:function(){return e.setNode(n)},transform:{x:40*o.position.i,y:40*o.position.j}}))}};for(var o in a)n(o)}return t}},{key:"drawEdges",value:function(){var e={},t=[];if(this.props.data&&this.props.data.edges){var a=this.props.data.edges;if(a)for(var n in a)if(a.hasOwnProperty(n)&&a[n]){var o=a[n].path,i=a[n].origin===this.state.activeNode?1:.5,s=void 0;if(o)for(var c=0;c<o.length;c++){var d=o[c];if(0!==c){var l=40*s.i,h=40*s.j,p=(d.j-s.j)*(s.i===d.i?2:1),m={x:l,y:h,rotate:p,opacity:i},u="".concat(l).concat(h).concat(p);e[u]||(e[u]=[]),1===i?e[u].splice(0,0,m):e[u].push(m)}s=d}}}for(var v in e)if(e.hasOwnProperty(v)){var f=e[v][0];t.push(r.a.createElement(y,{key:v,transform:{x:f.x,y:f.y,rotate:f.rotate},opacity:f.opacity}))}return t}},{key:"shouldComponentUpdate",value:function(e,t,a){return this.props.data!==e.data||this.state.activeNode!==t.activeNode}},{key:"render",value:function(){return r.a.createElement("div",{className:"graph",style:this.props.data&&{height:40*this.props.data.height,width:40*this.props.data.width}},this.drawEdges(),this.drawNodes())}}]),a}(r.a.Component),N=a(106),g=a(107),O=a(104),j=(a(66),a(44)),k=a.n(j),C=a(45),w=a.n(C),x=function(e){Object(p.a)(a,e);var t=Object(m.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this,e)).makeChips=n.makeChips.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"makeChips",value:function(){var e=[];if(this.props.children){var t,a=Object(u.a)(this.props.children);try{for(a.s();!(t=a.n()).done;){var n=t.value;e.push(r.a.createElement(g.a,{color:"secondary",key:n,label:n}))}}catch(o){a.e(o)}finally{a.f()}}return e}},{key:"render",value:function(){return r.a.createElement("div",{className:"node-card"},r.a.createElement("div",{className:"card-header"},r.a.createElement("div",{className:"button-container"},r.a.createElement("div",{className:"button-item",style:{backgroundColor:"rgb(97, 205, 187)"},onClick:this.props.onEdit},r.a.createElement("img",{src:k.a,alt:"edit-node"}))),r.a.createElement("div",{className:"node"},r.a.createElement("div",{className:"node-item",style:{backgroundColor:"rgb(97, 205, 187)"}},r.a.createElement("p",null,this.props.name))),r.a.createElement("div",{className:"button-container"},r.a.createElement("div",{className:"button-item",style:{backgroundColor:"rgb(244,117,96)"},onClick:this.props.onRemove},r.a.createElement("img",{src:w.a,alt:"remove-node"})))),r.a.createElement("div",{className:"card-content"},this.makeChips()))}}]),a}(r.a.Component),S=function(e){Object(p.a)(a,e);var t=Object(m.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this,e)).state={children:[],node_name:"",child:"",nodes:{A:["B","C"],B:["D","E"],C:["D","E"],D:["F"],E:["F","G"],F:["G"],G:[]}},n.addChild=n.addChild.bind(Object(h.a)(n)),n.addNode=n.addNode.bind(Object(h.a)(n)),n.createNodeCards=n.createNodeCards.bind(Object(h.a)(n)),n.removeChild=n.removeChild.bind(Object(h.a)(n)),n.removeNode=n.removeNode.bind(Object(h.a)(n)),n.editNode=n.editNode.bind(Object(h.a)(n)),n.compileGraph=n.compileGraph.bind(Object(h.a)(n)),n.clean=n.clean.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"clean",value:function(){this.setState({children:[],node_name:"",child:"",nodes:{}})}},{key:"compileGraph",value:function(){var e=this,t=this.state.nodes;if(Object.keys(t).length>0){var a={method:"POST",mode:"cors",cache:"no-cache",credentials:"same-origin",headers:{"Content-Type":"application/json"},redirect:"follow",referrerPolicy:"no-referrer",body:JSON.stringify({nodes:t})};fetch("/api/compile",a).then((function(e){return e.json()})).then((function(t){t.error||e.setState({graph:t})}))}}},{key:"addNode",value:function(){if(""!==this.state.node_name){var e=this.state.nodes;e[this.state.node_name]=Object(c.a)(this.state.children),this.setState({children:[],node_name:"",child:"",nodes:e})}}},{key:"createNodeCards",value:function(){var e=this,t=[],a=this.state.nodes,n=function(n){a.hasOwnProperty(n)&&t.push(r.a.createElement(x,{key:n,name:n,children:a[n],onRemove:function(){return e.removeNode(n)},onEdit:function(){return e.editNode(n)}}))};for(var o in a)n(o);return t}},{key:"addChild",value:function(e){if("Enter"===e.key){var t=this.state.children,a=this.state.child;""===a||t.includes(a)||(t.push(a),this.setState({children:t,child:""}))}}},{key:"removeChild",value:function(e){var t=this.state.children,a=t.indexOf(e);a>-1&&(t.splice(a,1),this.setState({children:t}))}},{key:"removeNode",value:function(e){var t=this.state.nodes;t[e]&&(delete t[e],this.setState({nodes:t}))}},{key:"editNode",value:function(e){var t=this.state.nodes;if(t[e]){var a=t[e];delete t[e],this.setState({nodes:t,children:a,node_name:e})}}},{key:"componentDidMount",value:function(){this.compileGraph()}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"App"},r.a.createElement("h2",null,"Graph Display"),r.a.createElement("div",{className:"actions"},r.a.createElement("div",{className:"form"},r.a.createElement(N.a,{id:"node_name",style:{width:90},label:"Node Name",value:this.state.node_name,onChange:function(t){return e.setState({node_name:t.target.value})}}),r.a.createElement(N.a,{id:"child",style:{width:90},label:"Add Child",value:this.state.child,onChange:function(t){return e.setState({child:t.target.value})},onKeyPress:this.addChild})),r.a.createElement("div",{style:{width:40}}),r.a.createElement("div",null,r.a.createElement("h3",null,"Children"),r.a.createElement("div",{className:"children-panel"},this.state.children.map((function(t){return r.a.createElement(g.a,{key:t,onDelete:function(){return e.removeChild(t)},label:t})}))))),r.a.createElement("div",{className:"action-buttons"},r.a.createElement(O.a,{variant:"contained",color:"secondary",onClick:this.addNode},"Add Node"),r.a.createElement(O.a,{variant:"contained",color:"secondary",onClick:this.clean},"Clean"),r.a.createElement(O.a,{variant:"contained",color:"secondary",disabled:Object.keys(this.state.nodes).length<1,onClick:this.compileGraph},"Compile")),r.a.createElement("div",{className:"node-cards"},this.createNodeCards()),r.a.createElement("div",{className:"App-content"},r.a.createElement(E,{data:this.state.graph})))}}]),a}(r.a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var _=a(47),G=Object(_.a)({palette:{primary:{main:"rgb(97, 205, 187)"},secondary:{main:"rgb(244,117,96)"}}});i.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(s.a,{theme:G},r.a.createElement(S,null))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[57,1,2]]]);
//# sourceMappingURL=main.4c44000f.chunk.js.map