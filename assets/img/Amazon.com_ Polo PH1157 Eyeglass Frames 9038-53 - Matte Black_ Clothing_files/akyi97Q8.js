(function(){var k=this,l=function(a){return"string"==typeof a},m=function(a,b,c){return a.call.apply(a.bind,arguments)},n=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}},p=function(a,b,c){p=Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?m:n;return p.apply(null,
arguments)};var q=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,"")},r=function(a,b){return a<b?-1:a>b?1:0};var t;a:{var u=k.navigator;if(u){var v=u.userAgent;if(v){t=v;break a}}t=""};var x=function(a,b){var c=w;Object.prototype.hasOwnProperty.call(c,a)||(c[a]=b(a))};var y=-1!=t.indexOf("Opera"),z=-1!=t.indexOf("Trident")||-1!=t.indexOf("MSIE"),A=-1!=t.indexOf("Edge"),B=-1!=t.indexOf("Gecko")&&!(-1!=t.toLowerCase().indexOf("webkit")&&-1==t.indexOf("Edge"))&&!(-1!=t.indexOf("Trident")||-1!=t.indexOf("MSIE"))&&-1==t.indexOf("Edge"),C=-1!=t.toLowerCase().indexOf("webkit")&&-1==t.indexOf("Edge"),D=function(){var a=k.document;return a?a.documentMode:void 0},E;
a:{var F="",G=function(){var a=t;if(B)return/rv\:([^\);]+)(\)|;)/.exec(a);if(A)return/Edge\/([\d\.]+)/.exec(a);if(z)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(C)return/WebKit\/(\S+)/.exec(a);if(y)return/(?:Version)[ \/]?(\S+)/.exec(a)}();G&&(F=G?G[1]:"");if(z){var H=D();if(null!=H&&H>parseFloat(F)){E=String(H);break a}}E=F}
var I=E,w={},J=function(a){x(a,function(){for(var b=0,c=q(String(I)).split("."),d=q(String(a)).split("."),e=Math.max(c.length,d.length),f=0;0==b&&f<e;f++){var h=c[f]||"",g=d[f]||"";do{h=/(\d*)(\D*)(.*)/.exec(h)||["","","",""];g=/(\d*)(\D*)(.*)/.exec(g)||["","","",""];if(0==h[0].length&&0==g[0].length)break;b=r(0==h[1].length?0:parseInt(h[1],10),0==g[1].length?0:parseInt(g[1],10))||r(0==h[2].length,0==g[2].length)||r(h[2],g[2]);h=h[3];g=g[3]}while(0==b)}return 0<=b})},K;var L=k.document;
K=L&&z?D()||("CSS1Compat"==L.compatMode?parseInt(I,10):5):void 0;var M;if(!(M=!B&&!z)){var N;if(N=z)N=9<=Number(K);M=N}M||B&&J("1.9.1");z&&J("9");var O=function(a){return a?a.parentWindow||a.defaultView:window};var P=function(a){var b=O();b.google_image_requests||(b.google_image_requests=[]);var c=b.document.createElement("img");c.src=a;b.google_image_requests.push(c)};var Q=function(a){return"//pagead2.googlesyndication.com/pagead/gen_204?id=sodar&v=7&t="+a},R=function(a,b,c){a=Q(1)+"&e="+a;c&&(a+="&li="+encodeURIComponent(String(c)));b&&(a+="&bgai="+encodeURIComponent(String(b)));P(a)},T=function(a,b){return function(){try{return a.apply(this,arguments)}catch(g){if(!(1<=S)){var c=Q(0)+"&c="+encodeURIComponent(String(b))+"&ex=",d=g.toString();g.name&&-1==d.indexOf(g.name)&&(d+=": "+g.name);g.message&&-1==d.indexOf(g.message)&&(d+=": "+g.message);if(g.stack){var e=
g.stack,f=d;try{-1==e.indexOf(f)&&(e=f+"\n"+e);for(var h;e!=h;)h=e,e=e.replace(/((https?:\/..*\/)[^\/:]*:\d+(?:.|\n)*)\2/,"$1");d=e.replace(/\n */g,"\n")}catch(Z){d=f}}c+=encodeURIComponent(String(d));2E3<c.length?R(11):P(c);S+=1}}}},S=0,U=function(a,b){b=T(b,"i:lh");a.addEventListener?a.addEventListener("load",b,!1):a.attachEvent&&a.attachEvent("onload",b);return b},V=function(a,b){var c,d=b;c=U(a,function(){if(d){var b=d;d=null;a.removeEventListener?a.removeEventListener("load",c,!1):a.detachEvent&&
a.detachEvent("onload",c);return b.apply(this,arguments)}})};var W=function(a){var b;a:{b=typeof a;if("object"==b&&null!=a||"function"==b)switch(a["0"]){case "0":b="0"===a["0"]&&l(a["1"])&&l(a["2"])&&l(a["3"])&&l(a["4"])?!0:!1;break a}b=!1}if(!b)return null;b=[];for(var c in a)b.push(encodeURIComponent(c)+"="+encodeURIComponent(a[c]));return b.join("&")};var X=function(){var a=O().GoogleTyFxhY;if(!a)return R(0),null;if(0==a.length)return R(1),null;a=a.shift();return a._scs_&&a._bgu_&&a._bgp_?a:(R(2),null)},Y=function(a,b,c,d,e){var f;a:{try{f=a.contentWindow||(a.contentDocument?O(a.contentDocument):null);break a}catch(g){}f=null}if(f){a=(0==a.src.indexOf("https:")?"https":"http")+"://tpc.googlesyndication.com";var h={0:"0"};h["1"]=b;h["2"]=c;h["3"]=d;e||(e="");h["4"]=e;f.postMessage(W(h),a)}else R(3)};(function(a,b,c){T(a,b).apply(null,Array.prototype.slice.call(arguments,2))})(function(){var a=O().postMessage?!0:!1,b=!1,c=null,d=null,e=X();if(e)if(b=!0,c=e._scs_,d=e._li_,a){var f=document.createElement("iframe");V(f,p(Y,null,f,e._scs_,e._bgu_,e._bgp_,e._li_));f.src="//tpc.googlesyndication.com/sodar/adXpYxnS.html";f.width="0";f.height="0";f.style.display="none";document.body.appendChild(f)}else R(8,c,d);"0.01"<Math.random()||(a="//pagead2.googlesyndication.com/pagead/gen_204?id=sodarir&v=7&d="+
(b?1:0)+"&s="+(a?1:0)+"&f=0.01",d&&(a+="&li="+encodeURIComponent(String(d))),c&&(a+="&bgai="+encodeURIComponent(String(c))),P(a))},"i:i");})()
