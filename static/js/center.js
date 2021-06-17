
$.ajax({
        type:"GET",
        url:"center",
        dataType:"json",
        success:function (data){
            $("#name").append(data["name"]);
            $("#fiscode").append(data["fiscode"]);
            $("#age").append(data["age"]);
            $("#gender").append(data["gender"]);
            $("#nation").append(data["nation"]);
            document.getElementById("image").src = data['picture'];
            }
    });

    window.onresize = function(){
        resetContentPos(); // 调整页面水平居中
    }