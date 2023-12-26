class Bitcoin_Cypher:
  @staticmethod
  def retrieve_transaction(address, limit, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL bitcoin.retrieve.transaction(
          '{address}',
          {limit},
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
  def retrieve_transaction(address, limit, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL ethereum.retrieve.transaction(
          '{address}',
          {limit},
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
  def retrieve_token_transfer(address, limit, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL ethereum.retrieve.tokenTransfer(
          '{address}',
          {limit},
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
  def retrieve_transaction(address, limit, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL tron.retrieve.transaction(
          '{address}',
          {limit},
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
  def retrieve_token_transfer(address, limit, startTime, endTime, minValue, maxValue, reverse):
    return (
      f"""
        CALL tron.retrieve.tokenTransfer(
          '{address}',
          {limit},
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