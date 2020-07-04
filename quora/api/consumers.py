from asgiref.sync import async_to_sync 
from channels.generic.websocket import WebsocketConsumer
import json
from quans.models import Question

class ApiConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name='api'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )    

    def receive(self, text_data):
        text_data_json=json.load(text_data)
        title=text_data_json['title']
        content=text_data_json['body']
        submitted_by=text_data_json['submitted_by']
        id=text_data_json['id']

        question=Question.objects.get(pk=id)
        question.title=title
        question.body=body
        question.save()     
     
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'add_question',
                'title':title,
                'body':body,
                'submitted_by':submitted_by,
                'id':id,

            }
        )

    def add_question(self, event):
        title=event['title']
        content=event['body']
        id=event['id']

        #then send it to the websocket
        self.send(text_data=json.dumps({
            'title':title,
            'body':body,
            'id':id
        }))    