"""
Notes on Zulip Objects:

user_groups -- dictionaries with 'users', 'name'
streams -- dictionaries with 'name', 'description' (https://zulipchat.com/api/get-streams)
principals -- list of user_id's or zulip_email's

"""

#######################
        
def subscribe_usergroup_to_stream(my_user_group,my_stream):
    """
    Takes the Zulip format of user groups and users
    """
    my_users = my_user_group['users'] #returns user id
    return client.add_subscriptions(my_stream,myusers)
    
    
def get_usergroup_from_groupname(groupname):
    """
    group_name needs to be a string for the group.
    """
    some_weird_dictionary = client.get_user_groups() #maybe this should only be run once and we keep track of the dictionary
    list_of_dicts = some_weird_dictionary['user_groups']
    return list_of_dicts
    
    
def get_stream_from_streamname(mystreamname):
    some_weird_dictionary = client.get_streams()
    list_of_streams = weird_dictionary['streams']
    my_list_of_streams = match_key(list_of_streams,'name',mystreamname)
    return my_list_of_streams
    
    
def mod_subscribe_usergroup_to_stream(mygroupname,mystreamname):
    """
    
    """
    my_user_group = get_users_from_groupname(mygroupname)
    subscribe_usergroup_to_stream(my_user_group,mystreamname)



            
