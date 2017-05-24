import redis
config = {"host":"localhost", "port":6379}
r = redis.StrictRedis(**config)
r.set("user-1-profile","12:1.0,13:1.0,14:3.0,15:1.0,17:1.0,18:1.0,19:1.0,20:1.0,23:1.0,24:5.0,92:1.0,99:3.0,102:1.0,103:1.0,104:1.0,105:2.0,106:1.0,107:1.0,108:1.0,110:3.0,111:1.0,115:1.0,116:2.0,117:2.0,119:1.0,120:4.0,121:2.0,122:2.0,123:1.0,124:2.0,125:1.0,128:2.0,129:1.0,136:1.0,145:1.0,146:1.0,147:2.0,148:1.0,149:1.0,150:2.0,219:3.0,220:1.0,221:4.0,223:1.0,224:3.0,234:1.0,235:1.0,236:5.0,239:1.0,241:1.0,242:1.0,244:2.0,250:1.0,255:1.0,257:3.0,258:1.0,259:1.0,260:1.0,261:2.0,262:1.0,263:1.0,265:1.0,267:1.0,268:1.0,269:3.0,272:1.0,273:4.0,274:2.0,275:2.0,276:1.0,277:2.0,278:1.0,279:4.0,280:2.0,281:4.0,282:2.0,283:2.0,284:2.0,285:1.0,286:1.0,287:4.0,288:4.0,289:2.0,290:2.0,291:1.0,293:2.0,298:1.0,299:3.0,300:1.0,301:1.0,302:1.0,303:1.0,304:1.0,305:1.0,306:1.0,307:1.0,318:3.0,320:2.0,321:1.0,322:2.0,323:1.0,324:2.0,325:1.0,326:2.0,327:3.0,328:1.0,329:1.0,330:1.0,331:2.0,332:3.0,333:1.0,334:1.0,335:2.0,336:1.0,357:2.0,358:1.0,359:1.0,362:1.0,367:1.0,368:3.0,369:2.0,404:4.0,405:1.0,406:2.0,407:1.0,408:1.0,409:1.0,410:3.0,411:2.0,412:2.0,423:1.0,454:1.0,455:1.0,456:1.0,457:3.0,458:1.0,459:1.0,470:1.0,471:1.0,472:1.0,474:2.0,475:4.0,476:1.0,507:2.0,543:1.0,545:2.0,546:1.0,590:3.0,592:1.0,594:1.0,595:3.0,596:2.0,597:1.0,618:3.0,619:1.0,627:2.0,675:3.0,677:2.0,679:1.0,680:1.0,681:4.0,682:1.0,684:1.0,686:1.0,687:1.0,689:3.0,695:1.0,712:1.0,716:1.0,717:1.0,739:1.0,740:1.0,741:3.0,742:1.0,743:2.0,747:1.0,748:1.0,755:1.0,757:1.0,759:1.0,761:1.0,762:1.0,763:1.0,765:1.0,766:1.0,812:1.0,814:2.0,817:1.0,818:2.0,819:1.0,822:2.0,823:1.0,824:1.0,825:1.0,826:2.0,827:1.0,828:1.0,830:1.0,831:1.0,832:1.0,833:1.0,839:1.0,840:1.0,843:1.0,844:3.0,845:2.0,846:1.0,863:1.0,865:1.0,869:1.0,870:1.0,871:1.0,872:1.0,873:1.0,874:3.0,875:1.0,876:1.0,877:1.0,878:1.0,879:1.0,880:1.0,881:1.0,882:1.0,883:1.0,884:1.0,885:1.0,886:1.0,918:1.0,919:1.0,921:1.0,923:2.0,924:1.0,925:1.0,926:1.0,927:3.0,928:1.0,929:1.0,930:1.0,931:1.0,932:1.0,933:2.0,936:2.0,937:1.0,947:1.0,949:1.0,951:1.0,973:3.0,974:1.0,975:1.0,976:1.0,977:1.0,978:1.0,979:1.0,980:1.0,981:1.0,982:1.0,983:1.0,984:1.0,985:1.0,987:2.0,988:1.0,989:1.0,990:1.0,994:1.0,1000:1.0,1001:1.0,1007:1.0,1008:1.0,1009:1.0,1010:1.0,1014:1.0,1016:1.0,1021:1.0,1024:1.0,1025:1.0,1027:2.0,1032:1.0,1033:1.0,1037:1.0,1039:1.0,1046:2.0,1047:2.0,1048:1.0,1050:1.0,1051:1.0,1053:2.0,1056:1.0,1058:1.0,1059:1.0,1060:1.0,1066:1.0,1067:1.0,1078:1.0,1080:1.0,1083:1.0,1084:1.0,1085:1.0,1086:1.0,1092:1.0,1093:1.0,1094:1.0,1096:1.0,1101:1.0,1113:1.0,1114:1.0,1116:2.0,1119:1.0,1127:1.0,1128:1.0,1131:1.0,1133:2.0,1136:1.0,1149:1.0,1150:1.0,1151:2.0,1160:1.0,1161:1.0,1162:2.0,1163:2.0,1164:1.0,1170:1.0,1172:1.0,1173:1.0,1186:1.0,1196:1.0,1197:1.0,1198:1.0,1201:1.0,1214:1.0,1241:1.0,1244:1.0,1251:1.0,1254:1.0,1258:1.0,1264:1.0,1271:1.0,1275:1.0,1276:1.0,1279:1.0,1280:1.0,1281:1.0,1283:1.0,1286:1.0,1287:1.0,1288:1.0,1290:1.0,1294:1.0,1295:1.0,1301:1.0,1311:1.0,1316:1.0,1317:1.0,1318:1.0,1319:1.0,1320:1.0,1321:1.0,1322:1.0,1323:1.0,1324:1.0,1325:1.0,1326:1.0,1327:1.0,1328:1.0,1329:1.0,1330:1.0,1331:1.0,1332:1.0,1333:1.0,1334:1.0,1335:1.0,1336:1.0,1337:1.0,1338:1.0,1339:1.0,1340:1.0,1341:1.0,1342:1.0,1343:1.0,1344:1.0,1345:1.0,1346:1.0,1347:1.0,1348:1.0,1349:1.0,1350:1.0,1351:1.0,1352:1.0,1353:1.0,1354:1.0,1355:1.0,1356:1.0,1357:1.0,1358:1.0,1359:1.0,1360:1.0,1361:1.0,1362:1.0,1363:1.0,1364:1.0,1365:1.0,1366:1.0,1367:1.0,1368:1.0,1369:1.0,1370:1.0,1371:1.0,1372:1.0,1373:1.0,1374:1.0,1375:1.0,1376:1.0,1377:1.0,1378:1.0,1379:1.0,1380:1.0,1381:1.0,1382:1.0,1383:1.0,1384:1.0,1385:1.0,1386:1.0,1387:1.0,1388:1.0,1389:1.0,1390:1.0,1391:1.0,1392:1.0,1393:1.0,1394:1.0,1699:26.0,1701:6.0,1799:435.0,1801:0.2,1802:0.11,1803:0.04,1804:0.09,1805:0.43,1806:0.09,1807:3.0,1808:0.67,1809:2.0,1810:0.01,1811:0.06,1812:0.04,1813:0.07,1814:0.24,1815:0.09,1816:0.32,1817:0.06")
r.set("user-2-profile","4:5,5:4,7:4,8:5,9:4,11:5,12:5,15:3,17:4,19:3,21:3,22:4,23:5,24:4,25:4,28:3,30:4,31:3,32:5,42:4,44:4,45:4,47:4,48:4,49:3,50:5,54:2,55:3,56:5,58:3,59:4,60:3,61:3,64:4,65:3,66:4,68:4,69:2,70:4,71:4,72:4,73:3,74:4,77:3,79:4,81:5,82:4,85:4,87:4,88:4,89:5,91:4,92:4,95:4,96:4,97:1,98:3,99:4,100:5,107:4,109:3,116:4,117:3,118:3,121:3,122:4,123:3,124:4,127:4,129:5,131:4,132:3,133:3,134:5,135:5,139:3,141:3,143:4,144:3,147:3,148:3,151:4,152:5,153:5,154:4,156:4,157:5,160:4,161:3,162:4,163:4,164:4,165:3,166:3,168:4,169:5,170:3,171:4,172:4,174:4,175:5,176:4,177:5,178:4,179:4,180:5,181:4,182:5,183:4,184:4,185:4,186:4,187:5,191:4,192:5,193:3,194:5,195:5,196:3,197:3,198:3,199:4,200:5,201:5,202:4,203:5,204:4,205:3,208:4,209:4,210:4,211:4,213:4,214:2,215:3,216:3,218:5,219:3,223:4,226:3,230:4,231:3,233:3,234:3,235:3,237:3,238:5,239:3,241:4,248:4,254:2,255:4,257:4,259:3,264:2,265:3,273:2,274:3,275:4,276:4,283:3,284:4,285:5,288:4,291:3,293:4,294:3,295:3,298:5,309:1,313:3,318:4,319:4,321:3,322:2,356:3,357:4,365:3,367:4,371:3,378:3,382:4,385:4,392:4,393:4,396:4,402:4,403:4,404:3,408:5,410:4,411:4,417:3,419:4,420:4,423:5,425:4,427:4,428:5,429:4,430:4,432:4,433:5,434:4,435:4,436:4,443:3,447:4,448:3,449:3,452:2,455:4,461:4,463:4,466:5,467:4,469:5,471:3,472:2,473:3,475:4,477:4,479:5,480:4,481:4,482:5,483:3,484:3,485:3,486:4,487:4,488:4,490:4,492:3,493:3,494:5,495:3,496:3,498:5,499:3,501:4,502:5,504:4,505:3,506:4,507:3,509:4,510:3,511:5,512:5,513:3,514:4,515:3,516:4,517:4,519:4,520:4,521:3,522:3,523:4,525:5,526:3,528:3,530:4,531:4,537:4,546:3,550:4,558:4,559:4,566:4,567:4,568:5,569:3,578:2,579:3,581:4,582:3,583:4,584:4,588:5,589:4,591:3,597:3,602:4,603:5,605:4,607:3,609:4,610:4,611:4,613:4,614:3,615:3,616:2,618:4,628:3,629:4,632:3,633:4,634:4,637:3,640:4,641:4,642:5,646:5,648:4,649:4,653:5,654:5,655:4,656:3,657:4,659:3,660:3,661:4,663:5,664:5,665:4,671:4,673:4,675:4,678:3,679:4,684:3,686:4,692:3,693:3,699:4,705:5,708:4,709:3,712:4,715:5,729:3,732:4,736:3,739:4,741:4,742:4,746:4,747:3,755:3,770:4,778:3,792:3,802:3,805:4,806:4,811:4,822:4,824:3,825:4,826:3,842:3,843:3,848:4,853:5,856:4,863:3,921:4,928:4,942:3,945:4,959:3,962:4,965:4,966:3,968:4,1006:4,1019:4,1021:4,1028:2,1045:4,1046:4,1047:3,1065:5,1073:3,1074:3,1118:4,1121:3,1126:3,1135:4,1140:4,1147:4,1154:2,1169:5,1197:4,1211:3,1252:3,1286:3,1404:4,1411:4,1421:4,1456:4,1515:4,1700:60,1701:0,1702:16,1800:397,1801:0.00,1802:0.69,1803:0.39,1804:0.12,1805:0.23,1806:1.23,1807:0.37,1808:0.06,1809:1.52,1810:0.06,1811:0.14,1812:0.25,1813:0.27,1814:0.18,1815:0.61,1816:0.39,1817:0.77,1818:0.28,1819:0.09")
