function get_information(){
$.ajax({
           type:"get",
           url:'center',
           dataType:"json",
           success:function (datas){
           $(".num p").html(datas['name'])
           }
})
}
setInterval(get_information,timeout:1000)