from timebank.accounts.models import Account, Transaction,Transfer
def pass_currency(action,amount,user,payed_by,payed_to,appointment,comment):
    transaction=Transaction(appointment=appointment,
                               amount=amount,
                               payed_by=payed_by, 
                               payed_to=payed_to,
                               action=action,
                               comments=comment,
                               user=user,
                               title=appointment.service.title)
    transaction.save()
    to_ac=Account.objects.get(user=payed_to)
    by_ac=Account.objects.get(user=payed_by)
    
    to_ac.balance+=amount
    to_ac.save()
    by_ac.balance-=amount
    by_ac.save()
    tt=Transfer(user=payed_to,
                transaction=transaction,
                balance=to_ac.balance,
                amount=amount)
    tt.save()
    tb=Transfer(user=payed_by,
                transaction=transaction,
                balance=by_ac.balance,
                amount=amount*(-1))
    tb.save()
