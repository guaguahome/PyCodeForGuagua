#coding:utf8
__author__ = 'Administrator'

from twisted.spread import pb
from twisted.internet import  reactor

class Two(pb.Referenceable):
    def remote_print(self,arg):
        print "two.print was given", arg

class One(pb.Root):
    def __init__(self,two):
        self.two = two
    def remote_getTwo(self):
        print "One.getTwo(), returning my two called", self.two   #本地two， 并且客户端再次调用会还是这个对象
        return self.two

    def remote_checkTwo(self,newtwo):
        print "One.checkTwo(): comparing my two", self.two       #本地two， 并且客户端再次调用会还是这个对象,比如newtwo
        print "One.checkTwo(): aginst your two", newtwo
        if self.two == newtwo:
            print "One.checkTwo(): our twos are the same"

two = Two()
root_obj = One(two)
reactor.listenTCP(9013, pb.PBServerFactory(root_obj))
reactor.run()