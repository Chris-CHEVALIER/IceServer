# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.4
#
# <auto-generated>
#
# Generated from file `MP3Manager.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module AppServer
_M_AppServer = Ice.openModule('AppServer')
__name__ = 'AppServer'

if 'Track' not in _M_AppServer.__dict__:
    _M_AppServer.Track = Ice.createTempClass()
    class Track(Ice.Object):
        def __init__(self, id='', title='', artist='', album='', path=''):
            self.id = id
            self.title = title
            self.artist = artist
            self.album = album
            self.path = path

        def ice_ids(self, current=None):
            return ('::AppServer::Track', '::Ice::Object')

        def ice_id(self, current=None):
            return '::AppServer::Track'

        def ice_staticId():
            return '::AppServer::Track'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_AppServer._t_Track)

        __repr__ = __str__

    _M_AppServer.TrackPrx = Ice.createTempClass()
    class TrackPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_AppServer.TrackPrx.ice_checkedCast(proxy, '::AppServer::Track', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_AppServer.TrackPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::AppServer::Track'
        ice_staticId = staticmethod(ice_staticId)

    _M_AppServer._t_TrackPrx = IcePy.defineProxy('::AppServer::Track', TrackPrx)

    _M_AppServer._t_Track = IcePy.defineClass('::AppServer::Track', Track, -1, (), False, False, None, (), (
        ('id', (), IcePy._t_string, False, 0),
        ('title', (), IcePy._t_string, False, 0),
        ('artist', (), IcePy._t_string, False, 0),
        ('album', (), IcePy._t_string, False, 0),
        ('path', (), IcePy._t_string, False, 0)
    ))
    Track._ice_type = _M_AppServer._t_Track

    _M_AppServer.Track = Track
    del Track

    _M_AppServer.TrackPrx = TrackPrx
    del TrackPrx

if 'MP3Manager' not in _M_AppServer.__dict__:
    _M_AppServer.MP3Manager = Ice.createTempClass()
    class MP3Manager(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_AppServer.MP3Manager:
                raise RuntimeError('AppServer.MP3Manager is an abstract class')

        def ice_ids(self, current=None):
            return ('::AppServer::MP3Manager', '::Ice::Object')

        def ice_id(self, current=None):
            return '::AppServer::MP3Manager'

        def ice_staticId():
            return '::AppServer::MP3Manager'
        ice_staticId = staticmethod(ice_staticId)

        def add(self, track, current=None):
            pass

        def remove(self, title, current=None):
            pass

        def play(self, track, current=None):
            pass

        def search(self, key, value, current=None):
            pass

        def getTrackList(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_AppServer._t_MP3Manager)

        __repr__ = __str__

    _M_AppServer.MP3ManagerPrx = Ice.createTempClass()
    class MP3ManagerPrx(Ice.ObjectPrx):

        def add(self, track, _ctx=None):
            return _M_AppServer.MP3Manager._op_add.invoke(self, ((track, ), _ctx))

        def begin_add(self, track, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_AppServer.MP3Manager._op_add.begin(self, ((track, ), _response, _ex, _sent, _ctx))

        def end_add(self, _r):
            return _M_AppServer.MP3Manager._op_add.end(self, _r)

        def remove(self, title, _ctx=None):
            return _M_AppServer.MP3Manager._op_remove.invoke(self, ((title, ), _ctx))

        def begin_remove(self, title, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_AppServer.MP3Manager._op_remove.begin(self, ((title, ), _response, _ex, _sent, _ctx))

        def end_remove(self, _r):
            return _M_AppServer.MP3Manager._op_remove.end(self, _r)

        def play(self, track, _ctx=None):
            return _M_AppServer.MP3Manager._op_play.invoke(self, ((track, ), _ctx))

        def begin_play(self, track, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_AppServer.MP3Manager._op_play.begin(self, ((track, ), _response, _ex, _sent, _ctx))

        def end_play(self, _r):
            return _M_AppServer.MP3Manager._op_play.end(self, _r)

        def search(self, key, value, _ctx=None):
            return _M_AppServer.MP3Manager._op_search.invoke(self, ((key, value), _ctx))

        def begin_search(self, key, value, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_AppServer.MP3Manager._op_search.begin(self, ((key, value), _response, _ex, _sent, _ctx))

        def end_search(self, _r):
            return _M_AppServer.MP3Manager._op_search.end(self, _r)

        def getTrackList(self, _ctx=None):
            return _M_AppServer.MP3Manager._op_getTrackList.invoke(self, ((), _ctx))

        def begin_getTrackList(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_AppServer.MP3Manager._op_getTrackList.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTrackList(self, _r):
            return _M_AppServer.MP3Manager._op_getTrackList.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_AppServer.MP3ManagerPrx.ice_checkedCast(proxy, '::AppServer::MP3Manager', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_AppServer.MP3ManagerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::AppServer::MP3Manager'
        ice_staticId = staticmethod(ice_staticId)

    _M_AppServer._t_MP3ManagerPrx = IcePy.defineProxy('::AppServer::MP3Manager', MP3ManagerPrx)

    _M_AppServer._t_MP3Manager = IcePy.defineClass('::AppServer::MP3Manager', MP3Manager, -1, (), True, False, None, (), ())
    MP3Manager._ice_type = _M_AppServer._t_MP3Manager

    MP3Manager._op_add = IcePy.Operation('add', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_AppServer._t_Track, False, 0),), (), ((), IcePy._t_bool, False, 0), ())
    MP3Manager._op_remove = IcePy.Operation('remove', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_bool, False, 0), ())
    MP3Manager._op_play = IcePy.Operation('play', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_AppServer._t_Track, False, 0),), (), ((), IcePy._t_bool, False, 0), ())
    MP3Manager._op_search = IcePy.Operation('search', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_AppServer._t_Track, False, 0), ())
    MP3Manager._op_getTrackList = IcePy.Operation('getTrackList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_string, False, 0), ())

    _M_AppServer.MP3Manager = MP3Manager
    del MP3Manager

    _M_AppServer.MP3ManagerPrx = MP3ManagerPrx
    del MP3ManagerPrx

# End of module AppServer
