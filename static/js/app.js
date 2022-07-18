var socket = io("http://" + document.domain + ":" + location.port)

socket.on("user", function(json){

    console.log(json)
    $("#counter").text(json.counter)

})

socket.on("connect", function(){

    console.log("connected to web sockets")
})

socket.on("disconnect", function(){

    console.log("disconnected from web sockets")
})