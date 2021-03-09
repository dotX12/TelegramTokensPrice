from misc import *
from regex import *
from telethon import events
import time


@client.on(events.NewMessage(pattern=all_regex_one))
async def my_event_handler(event):
    cryptocurrency = event.raw_text.split()[1].lower()
    token_id = wrapper.get_id_from_symbol(cryptocurrency)
    if token_id:
        data_token = await wrapper.price_token(coin_id=token_id)
        msg = await event.reply(wrapper.get_formatted_text(data_token), parse_mode='md')
        flood.msg_list.append({'delete_time': time.time() + 30, 'data': {'chat_id': msg.to_id, 'msg_id': msg.id}})
    else:
        pass


@client.on(events.NewMessage(pattern=all_regex_pair))
async def my_event_handler(event):
    pairs = event.raw_text.split()[1].split('_')
    one_cryptocurrency = pairs[0].lower()
    two_cryptocurrency = pairs[1].upper()
    one_cryptocurrency_token_id = wrapper.get_id_from_symbol(one_cryptocurrency)
    if one_cryptocurrency_token_id:
        data_token = await wrapper.price_token(coin_id=one_cryptocurrency_token_id, currency=two_cryptocurrency)
        msg = await event.reply(wrapper.get_formatted_text(data_token, two_cryptocurrency), parse_mode='md')
        flood.msg_list.append({'delete_time': time.time() + 30, 'data': {'chat_id': msg.to_id, 'msg_id': msg.id}})
    else:
        pass
