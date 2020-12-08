f = open('covid_19_india.csv', 'r')
covid_data = {}
for lines in f:
    data = lines.rstrip('\n').split(',')
    #print(data)
    state, cured, deaths, confirmed = data[3].rstrip('***').lower(), data[6], data[7], data[8]
    #print(state,cured,deaths,confinmered)

    covid_data[state] = {'state': state, 'cured': cured, 'deaths': deaths, 'confirmed': confirmed }

#print(covid_data)

def CovidData(**kwargs):
    st = kwargs['state']
    prop = kwargs['property']
    if st in covid_data:
        #print(covid_data[st]['state'])
        pass
        if prop in covid_data[st]:
            print(prop,':',covid_data[st][prop])
        else:
            print('invalid key')
    else:
        print('state does not exist')


state = input("enter state")
property = input("enter property")
CovidData(state= state, property= property)


