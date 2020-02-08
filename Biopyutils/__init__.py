#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License           : GPL3
# Author            : Jingxin Fu <jingxinfu.tj@gmail.com>
# Date              : 07/02/2020
# Last Modified Date: 07/02/2020
# Last Modified By  : Jingxin Fu <jingxinfu.tj@gmail.com>
__version__ = "0.0.1"
import os
DATA_BASE =''

def getGeneRefPath(species,map_id):
    return os.path.join(DATA_BASE,'geneId_%s_%s.pickle.gz' % (species,map_id))

def getSpeciesRefPath(map_id):
    return os.path.join(DATA_BASE,'species_hg-mm_%s.pickle.gz' % (map_id))
