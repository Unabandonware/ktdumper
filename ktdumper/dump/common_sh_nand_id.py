class CommonShNandId:

    def parse_opts(self, opts):
        super().parse_opts(opts)

        self.NAND_CMD = opts["nand_cmd"]
        self.NAND_ADDR = opts["nand_addr"]
        self.NAND_DATA = opts["nand_data"]

    def read_id(self):
        self.writeb(0x90, self.NAND_CMD)
        self.writeb(0x00, self.NAND_ADDR)
        ret = b""
        for x in range(5):
            ret += bytes([self.readh(self.NAND_DATA) & 0xFF])
        return ret

    def execute(self, dev, output):
        super().execute(dev, output)

        print("=" * 80)
        print("NAND ID: {}".format(self.read_id().hex()))
        print("=" * 80)
