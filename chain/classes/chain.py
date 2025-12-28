from pydantic import BaseModel, Field
from typing import List, Optional, Any
from decimal import Decimal

from chain.classes.block import Block


class Chain(BaseModel):
    usdc_pool: Optional[Decimal]=Field(default=Decimal(0))
    tgt_pool: Optional[Decimal]=Field(default=Decimal(0))
    blocks: List[Block]=Field(default=[])
    mempool: List[Any]=Field(default=[])
    
    def __init__(self, **data):
        super().__init__(**data)
        self.tgt_pool = Decimal(1e10)
        self.genesis()
        
    def genesis(self):
        genesis_block = Block(
            index=0,
            prev_hash='000000000000000',
            data='GENESIS'
        )
        self.blocks.append(genesis_block)
        
    @property    
    def iter_blocks(self) -> List[dict]:
        return [] if not self.blocks else [block.model for block in self.blocks]
    
    @property
    def iter_pools(self) -> List[dict]:
        return [
            {'USDC': str(self.usdc_pool)},
            {'TGT': str(self.tgt_pool)}
        ]