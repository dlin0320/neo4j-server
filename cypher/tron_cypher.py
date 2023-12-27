def retrieve_transaction_query(address, startTime, endTime, minValue, maxValue, reverse):
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

def retrieve_token_transfer_query(address, startTime, endTime, minValue, maxValue, reverse):
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

def graph_transaction_query(address, timespan, maxRelationshipCount, startTime, minValue, maxValue, depth, reverse):
  return (
    f"""
      CALL tron.graph.transaction(
        "{address}",
        {timespan},
        {maxRelationshipCount},
        {startTime},
        {minValue},
        {maxValue},
        {depth},
        {reverse}
      )
      YIELD result
      RETURN result
    """
  )