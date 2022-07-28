# -----------------------------------------------------------
# opc ua signal to redis queue
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------


import asyncio
from asyncua import Client, Node, ua

# queue
import redis

"""
The goal of this script is to
- traverse available sensor nodes from an opc ua server
- create an asyncua subscription object to said nodes
- push updates to subscribed nodes into a redis queue
"""


opcua_server_url = "opc.tcp://MyPC.home:53530/OPCUA/SimulationServer"


async def main():

    client = Client(url=opcua_server_url)
    await client.connect()

    objects = client.get_objects_node()
    objects_children = await objects.get_children()
    for objects_child in objects_children:

        # all sensory nodes in default testserver are under sim
        if objects_child.nodeid.Identifier == "85/0:Simulation":
            nodes = await objects_child.get_children()
            for node in nodes:


    await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())
