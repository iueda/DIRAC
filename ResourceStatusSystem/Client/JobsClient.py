""" JobResultsClient class is a client for to get jobs' stats.
"""

from DIRAC.Core.Utilities.SitesDIRACGOCDBmapping import getGOCSiteName

from datetime import datetime, timedelta
from DIRAC.ResourceStatusSystem.Utilities.Exceptions import *
#from DIRAC.ResourceStatusSystem.Utilities.Utils import *

class JobsClient:
  
#############################################################################
  def getJobsStats(self, name, periods = None):
#forse qua non ho bisogno di un client... ce l'ho gia' in self.rc! Basta fare un buon command
    
    """  
    Return jobs stats of entity in name
    
    :params:
      :attr:`name`: should be the name of the ValidRes
    
      :attr:`periods`: optional list - contains the periods to consider in the query.
      If not given, takes the last 24h

    :return:
      {
        'MeanProcessedJobs': X'

        'LastProcessedJobs': X'
      }
    """
   
    #######TODO
#    numberOfJobsLash2Hours = self.rc.getReport('Job', 'NumberOfJobs', 
#                                               datetime.utcnow()-timedelta(hours = 2), 
#                                               datetime.utcnow(), {granularity:[entity]}, 
#                                               'GridStatus')
#    numberOfJobsLash2Hours = self.rc.getReport('Job', 'NumberOfJobs', 
#                                               datetime.utcnow()-timedelta(hours = 2), 
#                                               datetime.utcnow(), {granularity:[entity]}, 
#                                               'GridStatus')
#    
#    for x in numberOfJobs['Value']['data'].itervalues():
#      total = 0
#      for y in x.values():
#        total = total+y
#      
#    print r


#############################################################################

  def getJobsEff(self, granularity, name, periods):
    """
    Return job stats of entity in args for periods
    
    :params:
      :attr:`granularity`: string - should be a ValidRes
    
      :attr:`name` should be the name of the ValidRes
    
      :attr:`periods`: list - contains the periods to consider in the query

    returns:
      {
        'JobsEff': X (0-1)'
      }
    """

    if granularity == 'Site':
      entity = getGOCSiteName(name)['Value']
      _granularity = 'Site'
    else:
      entity = name
      _granularity = 'GridCE'
    
    #######TODO
#    numberOfJobs = self.rc.getReport('Job', 'NumberOfJobs', 
#                                     datetime.utcnow()-timedelta(hours = 24), 
#                                     datetime.utcnow(), {self._granularity:[self_entity]}, 
#                                     'GridStatus')
    

#############################################################################

  def getSystemCharge(self):
    """ Returns last hour system charge, and the system charge of an hour before

        returns:
          {
            'LastHour': n_lastHour
            'anHourBefore': n_anHourBefore
          }
    """
    
    # qui ho bisogno dei running jobs
    
    #######TODO

#    numberOfJobsLastHour = self.rc.getReport('Job', 'TotalNumberOfJobs', 
#                                             datetime.utcnow()-timedelta(hours = 1), 
#                                             datetime.utcnow(), {}, 'Grid')
    
    
#############################################################################


  def getJobsSimpleEff(self, name, RPCWMSAdmin = None, timeout = None):
    """  
    Return simple jobs efficiency
    
    :params:
      :attr:`name`: string or list of string - Site name(s)
    
      :attr:`RPCWMSAdmin`: RPCClient to RPCWMSAdmin

    :return: {'SiteName':'Good'|'Fair'|'Poor'|'Idle'|'Bad'}
    """

    if RPCWMSAdmin is not None: 
      RPC = RPCWMSAdmin
    else:
      from DIRAC.Core.DISET.RPCClient import RPCClient
      RPC = RPCClient("WorkloadManagement/WMSAdministrator", timeout = timeout)

    res = RPC.getSiteSummaryWeb({'Site':name},[],0,500)
    if not res['OK']:
      raise RSSException, where(self, self.getJobsSimpleEff) + " " + res['Message'] 
    else:
      res = res['Value']['Records']
    
    effRes = {}
    
    if len(res) == 0:
      return None 
    for r in res:
      name = r[0]
      try:
        eff = r[16]
      except IndexError:
        eff = 'Idle'
      effRes[name] = eff 
    
    return effRes
  
#############################################################################
