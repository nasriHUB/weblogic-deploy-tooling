def filter_model(model):
    print 'Node manager filter'
    if 'topology' in model:
        topology = model['topology']
        if 'Machine' in topology:
            machine = topology['Machine']
            print('  Deleting ' + str(len(machine)) + ' node managers')
            del topology['Machine'] 
