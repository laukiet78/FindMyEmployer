from EmployerDecorator import EmployerDecorator


class Employer_Plan2_decorator(EmployerDecorator):
  def __init__(self, user):
      super(Employer_Plan2_decorator, self).__init__(user)

  def plan_rules(self,givenCount):
      print "This is for plan 1 for EmployerDecorator "
      plan1Count= 5
      allow = False
      if givenCount<=plan1Count:
        allow = True
      elif givenCount>plan1Count:
        allow = False
      return allow
