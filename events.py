from flask import session
from flask.ext.socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session['name']
    join_room(room)
    emit('status', {'msg': session['name'] + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def left(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session['name']
    emit('message', {'msg': session['name'] + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session['name']
    leave_room(room)
    emit('status', {'msg': session['name'] + ' has left the room.'}, room=room)

