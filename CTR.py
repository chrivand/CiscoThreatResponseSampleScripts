# this sample python script can be used to integrate solutions with Cisco Threat Response
# the script has an cross-launch function that will open CTR in a new tab of the default browser

# import libraries
import webbrowser

### function that takes list of observables and creates CTR link and launches in default browser
def CtrLauncher(observables):
    # base URL needed to append observables to
    baseCTRlink = "https://visibility.amp.cisco.com/#/investigate?q="

    # string that separates the observables from each other
    observableSeparator = "%0A"

    # first item needs to be added to base CTR link
    finalCTRlink = baseCTRlink + str(observables[0]) + observableSeparator

    # skip first item and loop through other list items
    for observable in observables[1:]:
        finalCTRlink += (observable + observableSeparator)

    # automatically open browser with CTR
    webbrowser.open(finalCTRlink)
    return

### EXECUTION SCRIPT

# example observable variables, use this to fill the list, add more variables
badIP = "79.172.193.32"
badURL = "http://ihaveabadreputation.com"
badDomain = "internetbadguys.com"
badHash = "d5e0e8694ddc0548d8e6b87c83d50f4ab85c1debadb106d6a6a794c3e746f4fa"
#otherObservable = "<input-other-observable>"

#initate list with observables
observables = []

# append list with observables, add more variables if more observables needed
observables.append(badIP)
observables.append(badURL)
observables.append(badDomain)
observables.append(badHash)
#observables.append(otherObservable)

# execute CtrLauncher
CtrLauncher(observables)
