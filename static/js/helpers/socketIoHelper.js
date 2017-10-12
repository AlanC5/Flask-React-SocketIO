var SocketIoHelper = {
	setup: function() {
		const socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    	socket.on('my response', function(msg) {
	        alert(msg.data);
	    });
	}
}

module.exports = SocketIoHelper