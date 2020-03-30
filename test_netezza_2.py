# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 06:17:51 2018

@author: XT21586
"""

from netezza_sqlalchemy import BYTEINT, ST_GEOMETRY
from sqlalchemy import create_engine, Table, Column, Integer

engine = create_engine('netezza://<username>:<password>@<dsn>')