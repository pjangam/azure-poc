def get_az(node_count):
    last_num = min(3, node_count) + 1
    availability_zones = list(map(lambda x: str(x), range(1, last_num)))
    return availability_zones


class AksConfig:
    def __init__(self, dictionary):
        self.resource_group = dictionary["resource_group"]
        self.cluster_name = dictionary["cluster_name"]
        self.location = dictionary["location"]
        self.dns_prefix = dictionary["dns_prefix"]

        self.agent_pools = []
        for agent_pool_dict in dictionary["agent_pools"]:
            self.agent_pools.append(AgentPool(agent_pool_dict))

        # optional fields
        self.tags = None
        if 'tags' in dictionary:
            self.tags = dictionary['tags']


class AgentPool:
    def __init__(self, dictionary):
        self.size = dictionary["size"]

        self.node_count = dictionary["node_count"]
        self.availability_zones = get_az(dictionary["node_count"])

        # Optional parameters
        self.profile_name = 'dfagentpool'
        if 'profile_name' in dictionary:
            self.profile_name = dictionary['profile_name']
        self.os_type = 'Linux'
        if "os" in dictionary:
            self.os_type = dictionary["os"]
