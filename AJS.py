# By.Xeberlhyn
# TeamPeopleBOTS


#SCRIIP ANTIJS KICK DAN CANCEL.

#== TAROK DI BAGIAN ATAS.
protectantijs = []


#============SCRRIIIIPPP ANTIJS
        if People.type == 19 or People.type == 32:
            try:
                if People.param1 in protectantijs:
                  if People.param3 in XeberMID:
                    if People.param2 not in Bots and People.param2 not in owner and People.param2 not in admin:
                        settings["blackList"][People.param2] = True
                        sw.acceptGroupInvitation(People.param1)
                        sw.kickoutFromGroup(op.param1,[People.param2])
                        G = sw.getGroup(People.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        invsend = 0
                        Ticket = sw.reissueGroupTicket(People.param1)
                        Xeberlhyn.acceptGroupInvitationByTicket(People.param1,Ticket)
                        sw.leaveGroup(People.param1)
                        Xeberlhyn.inviteIntoGroup(People.param1,[Zmid])
                        Xeberlhyn.sendMessage(People.param1,"⌬ AntiJS telah di invite ulang")
                    else:
                       pass
                if People.param3 in Zmid:
                    if People.param2 not in Bots and People.param2 not in owner and People.param2 not in admin:
                        Xeberlhyn.kickoutFromGroup(People.param1,[People.param2])
                        Xeberlhyn.inviteIntoGroup(People.param1,[Zmid])
                        Xeberlhyn.sendMessage(People.param1,"⌬ AntiJS telah di invite ulang")
                    else:
                        Xeberlhyn.kickoutFromGroup(People.param1,[People.param2])
                        Xeberlhyn.inviteIntoGroup(People.param1,[Zmid])
                        Xeberlhyn.sendMessage(People.param1,"⌬ AntiJS telah di invite ulang")
                if People.param2 not in Bots and People.param2 not in owner and People.param2 not in admin:
                    if People.param3 in admin:
                        if People.param1 in protectantijs:
                            settings["blackList"][People.param2] = True
                            Xeberlhyn.kickoutFromGroup(People.param1,[People.param2])
                            Xeberlhyn.findAndAddContactsByMid(People.param3)
                            Xeberlhyn.inviteIntoGroup(People.param1,[People.param3])
                            Xeberlhyn.sendMessage(People.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass



#=============================REMOTE CONTROL
                        elif 'Antijs ' in msg.text:
                            if msg._from in admin:
                                spl = msg.text.replace('Antijs ','')
                                if spl == 'on':
                                    if msg.to in protectantijs:
                                         msgs = "⌬ AntiJS telah diaktifkan"
                                    else:
                                         protectantijs.append(msg.to)
                                         ginfo = Xeberlhyn.getGroup(msg.to)
                                         msgs = ""
                                    Xeberlhyn.sendMessage(to, "⌬ AntiJS telah aktif")
                                elif spl == 'off':
                                      if msg.to in protectantijs:
                                           protectantijs.remove(msg.to)
                                           ginfo = Xeberlhyn.getGroup(msg.to)
                                           msgs = "⌬ AntiJS telah dinonaktifkan"
                                      else:
                                           msgs = ""
                                      Xeberlhyn.sendMessage(to, "⌬ AntiJS belum aktif")
