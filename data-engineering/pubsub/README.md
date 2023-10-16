# [Pub/Sub](https://cloud.google.com/pubsub/docs/overview)
- [Message](#message)
- [Topic](#topic)
- [Subscription](#subscription)

![image](https://github.com/vanessaaleung/data-science-notes/assets/24954551/09278dfb-f810-48f8-a977-8e34fd3fe1b9)

## Message
_The data that moves through the service_

## Topic
_A named resource that represents a feed of messages_
- To publish a message with Pub/Sub, a publisher application creates and sends messages to a topic.
- Publishers and subscribers can subscribe to or publish to any topic they have access to.
- After publishing a message to a topic, a subscriber can retrieve the message.
- A topic can have multiple subscriptions, but a given subscription belongs to a single topic.

## Subscription
- Publishers and subscribers can subscribe to or publish to any topic they have access to.
- After publishing a message to a topic, a subscriber can retrieve the message.
- A topic can have multiple subscriptions, but a given subscription belongs to a single topic.
- `ackDeadline`: The subscriber has a configurable, limited amount of time, to acknowledge the outstanding message. After the deadline passes, the message is no longer considered outstanding, and Pub/Sub attempts to redeliver the message.
