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


### Type of Subscription
- Pull subscriptions use a subscriber client to request messages from the Pub/Sub server.
  - Use case: Large volume of messages 
- Push subscriptions use the Pub/Sub server to initiate requests to your subscriber application to deliver messages.
- Export subscriptions: export messages directly to a Google Cloud resource.
  - Use case: no additional processing needed.
  - BigQuery subscriptions export data to a BigQuery table.
  - Cloud Storage subscriptions export data to a Cloud Storage bucket.

- With the push subscription, you have to specify an HTTP endpoint (on GCP or elsewhere) that consumes the message. It's a webhook pattern. If the platform endpoint scale automatically with the traffic (Cloud Run, Cloud Functions for example), the message rate can go very high!! And the HTTP return code stands for message acknowledgment.
- With the pull subscription, the client needs to open a connection to the subscription and then pull the message. The client needs to explicitly acknowledge the messages. Several clients can be connected at the same time. With the client library, the message is consumed with gRPC protocol and it's more efficient (in terms of network bandwidth) to receive and consume the message
