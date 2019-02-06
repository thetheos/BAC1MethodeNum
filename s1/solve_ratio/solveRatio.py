# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 0
#
# Canevas de départ....
#
# -------------------------------------------------------------------------
# 
# NE PAS AJOUTER D'INSTRUCTION import / from :-)
# Uiliser uniquement le langage Python de base sans package !

def solveRatio(phi):
    try:
        return [1-((1-phi)/(1-2*phi)), (1-phi)/(1-2*phi)]
    except:
        return

#print(solveRatio((1 + sqrt(5.0)) / 2))
#print(solveRatio(0.5))