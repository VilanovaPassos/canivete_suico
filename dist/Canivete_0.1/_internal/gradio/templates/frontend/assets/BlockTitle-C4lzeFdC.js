import{I as b}from"./Info-DY-Ge3jA.js";import"./Index-DVb_ROzf.js";const{SvelteComponent:g,attr:p,check_outros:w,create_component:k,create_slot:B,destroy_component:I,detach:c,element:j,empty:q,flush:d,get_all_dirty_from_scope:v,get_slot_changes:C,group_outros:N,init:S,insert:m,mount_component:T,safe_not_equal:z,set_data:A,space:D,text:E,toggle_class:a,transition_in:r,transition_out:h,update_slot_base:F}=window.__gradio__svelte__internal;function $(f){let e,o;return e=new b({props:{$$slots:{default:[G]},$$scope:{ctx:f}}}),{c(){k(e.$$.fragment)},m(l,s){T(e,l,s),o=!0},p(l,s){const u={};s&10&&(u.$$scope={dirty:s,ctx:l}),e.$set(u)},i(l){o||(r(e.$$.fragment,l),o=!0)},o(l){h(e.$$.fragment,l),o=!1},d(l){I(e,l)}}}function G(f){let e;return{c(){e=E(f[1])},m(o,l){m(o,e,l)},p(o,l){l&2&&A(e,o[1])},d(o){o&&c(e)}}}function H(f){let e,o,l,s;const u=f[2].default,i=B(u,f,f[3],null);let t=f[1]&&$(f);return{c(){e=j("span"),i&&i.c(),o=D(),t&&t.c(),l=q(),p(e,"data-testid","block-info"),p(e,"class","svelte-1gfkn6j"),a(e,"sr-only",!f[0]),a(e,"hide",!f[0]),a(e,"has-info",f[1]!=null)},m(n,_){m(n,e,_),i&&i.m(e,null),m(n,o,_),t&&t.m(n,_),m(n,l,_),s=!0},p(n,[_]){i&&i.p&&(!s||_&8)&&F(i,u,n,n[3],s?C(u,n[3],_,null):v(n[3]),null),(!s||_&1)&&a(e,"sr-only",!n[0]),(!s||_&1)&&a(e,"hide",!n[0]),(!s||_&2)&&a(e,"has-info",n[1]!=null),n[1]?t?(t.p(n,_),_&2&&r(t,1)):(t=$(n),t.c(),r(t,1),t.m(l.parentNode,l)):t&&(N(),h(t,1,1,()=>{t=null}),w())},i(n){s||(r(i,n),r(t),s=!0)},o(n){h(i,n),h(t),s=!1},d(n){n&&(c(e),c(o),c(l)),i&&i.d(n),t&&t.d(n)}}}function J(f,e,o){let{$$slots:l={},$$scope:s}=e,{show_label:u=!0}=e,{info:i=void 0}=e;return f.$$set=t=>{"show_label"in t&&o(0,u=t.show_label),"info"in t&&o(1,i=t.info),"$$scope"in t&&o(3,s=t.$$scope)},[u,i,l,s]}class M extends g{constructor(e){super(),S(this,e,J,H,z,{show_label:0,info:1})}get show_label(){return this.$$.ctx[0]}set show_label(e){this.$$set({show_label:e}),d()}get info(){return this.$$.ctx[1]}set info(e){this.$$set({info:e}),d()}}export{M as B};
//# sourceMappingURL=BlockTitle-C4lzeFdC.js.map
