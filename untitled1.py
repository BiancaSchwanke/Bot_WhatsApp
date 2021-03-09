#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:09:55 2021

@author: bianca
"""

from whatsapp_api.whatsapp_api import WhatsApp
import pandas as pd
from datetime import datetime

agenda = pd.read_csv('agenda_c.csv')
agenda['Timestamp'] = 0
wp = WhatsApp()

input('Enter quando carregar o QRcode')

for contato in agenda['Nome'].values:
    mensagem = agenda.loc[agenda['Nome'] == contato, 'Mensagem'].values
    wp.search_contact(contato)
    wp.send_message(mensagem)
    
agenda.to_csv('mensagens_enviadas.csv', index=False)
