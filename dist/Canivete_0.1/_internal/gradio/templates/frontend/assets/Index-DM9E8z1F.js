import{B as z}from"./Button-DdWstpV4.js";import{S as D}from"./Index-DVb_ROzf.js";import E from"./Index-DPZ1xWbu.js";import"./index-DmVQEACr.js";import"./svelte/svelte.js";const{SvelteComponent:F,append:p,attr:C,create_slot:G,detach:q,element:h,flush:I,get_all_dirty_from_scope:H,get_slot_changes:J,init:K,insert:B,listen:L,safe_not_equal:M,set_data:N,set_style:k,space:j,text:O,toggle_class:A,transition_in:P,transition_out:Q,update_slot_base:R}=window.__gradio__svelte__internal;function T(o){let e,n,t,l,i,c,u,_,m,a;const r=o[3].default,f=G(r,o,o[2],null);return{c(){e=h("button"),n=h("span"),t=O(o[1]),l=j(),i=h("span"),i.textContent="▼",c=j(),u=h("div"),f&&f.c(),C(n,"class","svelte-1w6vloh"),C(i,"class","icon svelte-1w6vloh"),k(i,"transform",o[0]?"rotate(0)":"rotate(90deg)"),C(e,"class","label-wrap svelte-1w6vloh"),A(e,"open",o[0]),k(u,"display",o[0]?"block":"none")},m(s,d){B(s,e,d),p(e,n),p(n,t),p(e,l),p(e,i),B(s,c,d),B(s,u,d),f&&f.m(u,null),_=!0,m||(a=L(e,"click",o[4]),m=!0)},p(s,[d]){(!_||d&2)&&N(t,s[1]),d&1&&k(i,"transform",s[0]?"rotate(0)":"rotate(90deg)"),(!_||d&1)&&A(e,"open",s[0]),f&&f.p&&(!_||d&4)&&R(f,r,s,s[2],_?J(r,s[2],d,null):H(s[2]),null),d&1&&k(u,"display",s[0]?"block":"none")},i(s){_||(P(f,s),_=!0)},o(s){Q(f,s),_=!1},d(s){s&&(q(e),q(c),q(u)),f&&f.d(s),m=!1,a()}}}function U(o,e,n){let{$$slots:t={},$$scope:l}=e,{open:i=!0}=e,{label:c=""}=e;const u=()=>n(0,i=!i);return o.$$set=_=>{"open"in _&&n(0,i=_.open),"label"in _&&n(1,c=_.label),"$$scope"in _&&n(2,l=_.$$scope)},[i,c,l,t,u]}class V extends F{constructor(e){super(),K(this,e,U,T,M,{open:0,label:1})}get open(){return this.$$.ctx[0]}set open(e){this.$$set({open:e}),I()}get label(){return this.$$.ctx[1]}set label(e){this.$$set({label:e}),I()}}const{SvelteComponent:W,add_flush_callback:X,assign:Y,bind:Z,binding_callbacks:y,create_component:v,create_slot:x,destroy_component:w,detach:ee,flush:g,get_all_dirty_from_scope:te,get_slot_changes:se,get_spread_object:le,get_spread_update:ne,init:oe,insert:ie,mount_component:S,safe_not_equal:ae,space:_e,transition_in:b,transition_out:$,update_slot_base:re}=window.__gradio__svelte__internal;function ue(o){let e;const n=o[7].default,t=x(n,o,o[9],null);return{c(){t&&t.c()},m(l,i){t&&t.m(l,i),e=!0},p(l,i){t&&t.p&&(!e||i&512)&&re(t,n,l,l[9],e?se(n,l[9],i,null):te(l[9]),null)},i(l){e||(b(t,l),e=!0)},o(l){$(t,l),e=!1},d(l){t&&t.d(l)}}}function fe(o){let e,n;return e=new E({props:{$$slots:{default:[ue]},$$scope:{ctx:o}}}),{c(){v(e.$$.fragment)},m(t,l){S(e,t,l),n=!0},p(t,l){const i={};l&512&&(i.$$scope={dirty:l,ctx:t}),e.$set(i)},i(t){n||(b(e.$$.fragment,t),n=!0)},o(t){$(e.$$.fragment,t),n=!1},d(t){w(e,t)}}}function ce(o){let e,n,t,l,i;const c=[{autoscroll:o[6].autoscroll},{i18n:o[6].i18n},o[5]];let u={};for(let a=0;a<c.length;a+=1)u=Y(u,c[a]);e=new D({props:u});function _(a){o[8](a)}let m={label:o[1],$$slots:{default:[fe]},$$scope:{ctx:o}};return o[0]!==void 0&&(m.open=o[0]),t=new V({props:m}),y.push(()=>Z(t,"open",_)),{c(){v(e.$$.fragment),n=_e(),v(t.$$.fragment)},m(a,r){S(e,a,r),ie(a,n,r),S(t,a,r),i=!0},p(a,r){const f=r&96?ne(c,[r&64&&{autoscroll:a[6].autoscroll},r&64&&{i18n:a[6].i18n},r&32&&le(a[5])]):{};e.$set(f);const s={};r&2&&(s.label=a[1]),r&512&&(s.$$scope={dirty:r,ctx:a}),!l&&r&1&&(l=!0,s.open=a[0],X(()=>l=!1)),t.$set(s)},i(a){i||(b(e.$$.fragment,a),b(t.$$.fragment,a),i=!0)},o(a){$(e.$$.fragment,a),$(t.$$.fragment,a),i=!1},d(a){a&&ee(n),w(e,a),w(t,a)}}}function me(o){let e,n;return e=new z({props:{elem_id:o[2],elem_classes:o[3],visible:o[4],$$slots:{default:[ce]},$$scope:{ctx:o}}}),{c(){v(e.$$.fragment)},m(t,l){S(e,t,l),n=!0},p(t,[l]){const i={};l&4&&(i.elem_id=t[2]),l&8&&(i.elem_classes=t[3]),l&16&&(i.visible=t[4]),l&611&&(i.$$scope={dirty:l,ctx:t}),e.$set(i)},i(t){n||(b(e.$$.fragment,t),n=!0)},o(t){$(e.$$.fragment,t),n=!1},d(t){w(e,t)}}}function de(o,e,n){let{$$slots:t={},$$scope:l}=e,{label:i}=e,{elem_id:c}=e,{elem_classes:u}=e,{visible:_=!0}=e,{open:m=!0}=e,{loading_status:a}=e,{gradio:r}=e;function f(s){m=s,n(0,m)}return o.$$set=s=>{"label"in s&&n(1,i=s.label),"elem_id"in s&&n(2,c=s.elem_id),"elem_classes"in s&&n(3,u=s.elem_classes),"visible"in s&&n(4,_=s.visible),"open"in s&&n(0,m=s.open),"loading_status"in s&&n(5,a=s.loading_status),"gradio"in s&&n(6,r=s.gradio),"$$scope"in s&&n(9,l=s.$$scope)},[m,i,c,u,_,a,r,t,f,l]}class ke extends W{constructor(e){super(),oe(this,e,de,me,ae,{label:1,elem_id:2,elem_classes:3,visible:4,open:0,loading_status:5,gradio:6})}get label(){return this.$$.ctx[1]}set label(e){this.$$set({label:e}),g()}get elem_id(){return this.$$.ctx[2]}set elem_id(e){this.$$set({elem_id:e}),g()}get elem_classes(){return this.$$.ctx[3]}set elem_classes(e){this.$$set({elem_classes:e}),g()}get visible(){return this.$$.ctx[4]}set visible(e){this.$$set({visible:e}),g()}get open(){return this.$$.ctx[0]}set open(e){this.$$set({open:e}),g()}get loading_status(){return this.$$.ctx[5]}set loading_status(e){this.$$set({loading_status:e}),g()}get gradio(){return this.$$.ctx[6]}set gradio(e){this.$$set({gradio:e}),g()}}export{ke as default};
//# sourceMappingURL=Index-DM9E8z1F.js.map