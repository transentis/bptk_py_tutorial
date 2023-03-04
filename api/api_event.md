---
title: Event
description: BPTK API Documentation for the Element class
keywords: agent-based modeling, bptk, bptk-py, python, business prototyping
---

# Event

## Event Constructor

**Event(name, sender_id, receiver_id, data=None)**

The Event class is used to capture event information. Each event has a name, the id of the sending agent, the id of the receiving agent an optionally also some data (the actual payload).

The data can be any datatype, typically it will be a dictionary. The framework itself doesn't access the data. The agent that receives the event has to know how to handle it. 

