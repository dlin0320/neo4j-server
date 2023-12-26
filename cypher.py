class Bitcoin_Cypher:
  @staticmethod
  def retrieve_transaction(address, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL bitcoin.retrieve.transaction(
          "{address}",
          null,
          {startTime},
          {endTime},
          {minValue},
          {maxValue},
          {reverse}
        )
        YIELD result
        RETURN result
      """
	)

class Ethereum_Cypher:
  @staticmethod
  def retrieve_transaction(address, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL ethereum.retrieve.transaction(
          "{address}",
          null,
          {startTime},
          {endTime},
          {minValue},
          {maxValue},
          {reverse}
        )
        YIELD result
        RETURN result
      """
    )
  
  @staticmethod
  def retrieve_token_transfer(address, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL ethereum.retrieve.tokenTransfer(
          "{address}",
          null,
          {startTime},
          {endTime},
          {minValue},
          {maxValue},
          {reverse}
        )
        YIELD result
        RETURN result
      """
    )
    

class Tron_Cypher:
  @staticmethod
  def retrieve_transaction(address, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL tron.retrieve.transaction(
          "{address}",
          null,
          {startTime},
          {endTime},
          {minValue},
          {maxValue},
          {reverse}
        )
        YIELD result
        RETURN result
      """
    )
  
  @staticmethod
  def retrieve_token_transfer(address, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL tron.retrieve.tokenTransfer(
          "{address}",
          null,
          {startTime},
          {endTime},
          {minValue},
          {maxValue},
          {reverse}
        )
        YIELD result
        RETURN result
      """
    )