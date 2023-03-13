from yoomoney import Authorize

Authorize(
      client_id="DA2390328B7E37FBDCE8F38AADB65BED00B39C57B782BE001B1D63DEB3F98735",
      redirect_uri="http://t.me/Pay_p2p2_bot",
      scope=["account-info",
             "operation-history",
             "operation-details",
             "incoming-transfers",
             "payment-p2p",
             "payment-shop",
             ]
      )

