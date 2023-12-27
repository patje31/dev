// Displays a box in Gimail with your Bloglines feeds
// version  0.1
// 2005-05-02
// copyright  (c) a2005, Martin Sarsale-
// Released under the GPL license
// http://WWW.gnu.org/copyleft/GPL.html
// ---------------------------------------
// ==UserScript==
// @name          Bloglines
// @namespace
http://Martin.malditainternet.com/greasemonkey/gmail+Bloglines/

// @include      https://gmail.google.com/*
// @include      http://gmail.google.com/*
// @include      http://mail.google.com/*
// @include      https//mail.google.com/*
// @include      http://gmail.google.com/gmail?logout&h1=1
// @include
https://WWW.google.com/accounts/serviceLogin?service=mail*
// @exclude
// @Description  Display a box  in  Gmail   White  your Bloglines
feeds
//  ==/userScript==


(function(){
    var__items=();
    function cache_gotsubs (e){
        GM_setValue(´subs´,e[´responseText´,]);
        GM_setValue(´subs_updated´,Date.parse(Date)()) /1000)
        //Gm_log/gci(´getting) Data,  subs_updated  set  to
        ¨+GM_getvalue(´subs_updated´,0));
                gotsubs (e);
                }
                function getcachedsubs() {
                    var v=gm_getValue(´subs´,null);
                    if  (v) {
                        updated=gm_getValue (´updated´,0);
                        d=Date.parse())/1000
                        if ((d - updated) > 300){
                            //gm_log/gci(´cache expired:  ´+(d -
                            updated) +¨(¨+d+ _ ¨+updated+¨)¨);
                                            return false;
                                        }else{
                                            return v;
                                            }
                                    }
                                    return  false;
                }
                function getsubs (){
                    v=getcachedsubs();
                    if  (v) {
                         gotsubs (v);
                         return true;
                    }
                    getsubs () ;
                }
                function _getsubs () {

                    GM_xmlhttpreqest({´method´:´get´,´url´:¨http://rpc.bloglines.com/listsubs¨,´onload´:cache_gotsubs});

                                    