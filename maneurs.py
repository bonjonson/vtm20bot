usual = {
    'атака с фланга и с тыла': "Если персонаж атакует своего противника с фланга, пул проверки его атаки увеличивается на один d10, а если с тыла, то на два d10.",
    'засада': "Засада — это атака, которая застаёт противника врасплох и позволяет нанести ему неожиданный удар. Атакующий персонаж проходит встречную проверку ловкости + скрытности против восприятия + бдительности противника. Если атакующий побеждает, он проводит одну свободную атаку против своей жертвы, причём каждый оставшийся у него успех увеличивает пул проверки этой атаки на один d10. В случае ничьей атакующий действует первым, но его жертва получает возможность предпринять защитный манёвр. Если выигрывает жертва, она замечает засаду, и инициатива определяется как обычно. Если жертва уже принимает участие в сражении, устроить засаду на неё не получится.",
    'множественные действия': "Если персонаж будет предпринимать в свой ход множественные действия, игрок должен заранее указать, сколько действий он намерен предпринять, и сразу распределить между ними доступный ему пул d10. Если персонаж намерен только защищаться, значит, в этот ход ему лучше использовать механику блоков, уклонений или парирования. Подробнее о множественных действиях рассказано в пятой главе (см. стр. 265) книги правил.",
    'отмена действия': "Если персонаж ещё не предпринимал заявленное действие, он может в любой момент отказаться от него, чтобы предпринять защитное действие (блок, уклонение или парирование). Для этого персонаж должен успешно пройти проверку воли (сложность 6) или просто потратить пункт воли (в данном случае персонаж может потратить пункт воли прямо в момент отмены действия — не нужно объявлять об этом в фазе инициативы, как обычно). Проверка воли считается рефлекторным действием. Правила блока, уклонения и парирования описаны в разделе «Защитные манёвры».",
    'перемещение': "Если персонаж переместится менее чем на половину расстояния, которое позволяет ему его скорость бега (см. стр. 276), он сможет предпринять другое действие как обычно. Некоторые сложные манёвры, связанные с перемещением (типа прыжков и прочей акробатики), также могут считаться отдельным действием.",
    'прицеливание': "Если персонаж хочет нанести удар или выстрелить в конкретную область мишени, сложность проверки атаки возрастает, но в случае успеха прицельная атака может иметь некоторые дополнительные эффекты — проигнорировать броню или укрытие, нанести дополнительный урон и т.п. (все подробности отдаются на откуп рассказчику).",
    'удар или выстрел вслепую': "Если персонаж ослеплён (или находится в полной темноте), сложность проверок атаки возрастает на два пункта, а точную дистанционную атаку провести вообще невозможно. Силы вроде Обострения чувств (Ясновидение 1 — см. стр. 251) и Глаз Зверя (Метаморфозы 1 — см. стр. 160) помогают нейтрализовать это осложнение.",
}

def_man = {
    "блок": "Проверка ловкости + драки позволяет персонажу использовать собственное тело для отражения вражеских атак в ближнем бою. Если персонаж не облачён в броню или не является адептом Стойкости, то он может блокировать только атаки, наносящие лёгкие повреждения.",
    "парирование": "Проверка ловкости + фехтования позволяет блокировать любую атаку в ближнем бою. Если персонаж атакует без оружия, а противник пытается блокировать его атаку оружием, которое обычно наносит тяжёлые повреждения, атакующий рискует сам получить урон: если встречную проверку выигрывает противник, он проходит проверку урона, пул которой равен урону его оружия, плюс один d10 за каждый оставшийся у него успех (не считая первого).",
    "уклонение": "Проверка ловкости + атлетики позволяет персонажу уклоняться от любых атак. Для уклонения от атак в ближнем бою нужно только свободное пространство и возможность свободно двигаться (в противном случае придётся ограничиться блоками и парированием). В перестрелке уклонение — это либо стремительный бросок на расстояние как минимум метра в ближайшее укрытие, либо (в случае отсутствия укрытия) не менее стремительный переход в положение лёжа. Пока персонаж лежит или остаётся в укрытии, на последующие дистанционные атаки против него будут действовать правила, описанные на стр. 298 книги правил",
    "поглощение урона": "Персонаж имеет шанс нейтрализовать наносимые повреждения при помощи проверки на прочность. Пул проверки на прочность равен показателю выносливости персонажа. Простые смертные могут проходить проверку на прочность только против лёгких повреждений за счёт естественной устойчивости организма к внешним воздействиям. Вампиры (и другие сверхъестественные существа) переносят урон гораздо лучше и могут проходить проверку на прочность против тяжёлых повреждений. В проверке на прочность против губительных повреждений можно применять только Дисциплину Стойкости. Кроме того, значение Стойкости прибавляется к пулу проверок на прочность против лёгких и тяжёлых повреждений (так, если персонаж обладает выносливостью 3 и Стойкостью 2, то пул его проверок на прочность против лёгких и тяжёлых повреждений будет равен пяти d10, но против губительных — всего двум d10). Если атака попадает в цель и наносит повреждение, жертва проходит проверку на прочность, которая считается рефлекторным действием: для того чтобы пройти проверку на прочность, персонажу не нужно тратить действие или предпринимать множественные действия. Если не сказано иное, сложность проверки на прочность равна 6. Каждый полученный успех нейтрализует одно полученное персонажем повреждение. Как и проверка урона, проверка на прочность не может закончиться провалом — только неудачей.",
}

at_man = {
    "бросок": "Персонаж бросается на противника, стремясь сбить его с ног. Сложность атаки возрастает на один пункт, но в случае успеха противник не только получает положенный урон, но и проходит проверку ловкости + атлетики (сложность 7); в случае неудачи персонаж сбивает противника с ног (см. стр. 300), а в случае успеха противник теряет равновесие и сложность всех его проверок на следующий ход возрастает на один пункт.",
    "длинное оружие": "Непросто прорваться к противнику на расстояние удара кулаком или ножом, если тот вооружён мечом или хотя бы длинной палкой. Пул проверки атаки персонажа, который атакует противника, вооружённого более длинным оружием, уменьшается на один d10.",
    "захват": "Эта атака не наносит урона, поскольку её цель — не убить противника, а взять его живым и, желательно, невредимым. В случае успеха персонаж берёт противника в захват и удерживает его до следующего его действия. Как только очередь доходит до противника, он проходит встречную проверку силы + драки против силы + драки персонажа. Если противник не побеждает, он тратит своё действие впустую и остаётся в захвате. Вырвавшись из захвата, противник может сразу действовать как обычно.",
    "клинч": "Если эта атака проходит успешно, атакующий входит со своей жертвой в клинч и при желании может нанести ей урон. Каждый последующий ход оба бойца продолжают действовать в порядке инициативы, но пока кто‑нибудь не разорвёт клинч, единственное, что могут делать противники, — это наносить друг другу равный своей силе урон (проверка атаки не требуется). Чтобы разорвать клинч, один из противников может пройти встречную проверку силы + драки против силы + драки противника. Если персонаж выигрывает, он выходит из клинча; если нет — он всегда может попытаться высвободиться на следующий ход.",
    "подсечка": "Персонаж бьёт противника по ногам, чтобы лишить его равновесия и уронить на землю. Сложность проверки атаки возрастает на один пункт, но противник не только получает урон, равный силе персонажа, но и проходит проверку ловкости + атлетики (сложность 8); в случае неудачи персонаж сбивает противника с ног (см. стр. 300). Персонаж также может провести подсечку при помощи посоха, цепи или другого подходящего оружия. Эффект будет тот же, но урон, который получит противник, зависит от типа оружия.",
    "разоружение": "Чтобы выбить оружие из рук противника, персонаж должен пройти проверку атаки с +1 к сложности. В случае успеха персонаж проходит проверку урона как обычно. Если количество полученных успехов больше, чем показатель силы противника, противник не получает повреждений, но при этом лишается своего оружия. При провале персонаж либо роняет собственное оружие, либо получает урон от оружия противника.",
    "удар когтями": "Этот манёвр доступен только вампирам с когтями вроде тех, что персонаж может отрастить при помощи сил «Когти Зверя» (Метаморфозы 2 — см. стр. 160) или «Искусство костей» (Преображение 3 — см. стр. 197). Когти есть и у некоторых других сверхъестественных существ, например у оборотней. Удар когтями причиняет либо губительные повреждения (если это Когти Зверя), либо тяжёлые (если они выращены при помощи Искусства костей).",
    "удар ногой": "Под этим манёвром может подразумеваться любой удар ногой — от простого пинка до удара в прыжке с разворота. Рассказчик может изменять модификаторы сложности и (или) урона по своему усмотрению в зависимости от того, что описывают игроки.",
    "удар оружием": "Размашистый удар, резкий выпад или короткий тычок (в зависимости от типа оружия). Параметры холодного оружия см. в одноимённой таблице на стр. 300.",
    "удар рукой": "Персонаж бьёт противника кулаком. Это обычная безоружная атака в ближнем бою. Рассказчик может изменять модификаторы сложности и (или) урона по своему усмотрению в зависимости от типа удара (хук, джеб, апперкот или какой‑нибудь хитрый приём карате).",
    "укус": "Этот манёвр доступен только вампирам (и другим сверхъестественным существам вроде оборотней). В данном случае имеется в виду «боевой» укус, рассчитанный на то, чтобы нанести урон, а не на то, чтобы просто пустить жертве кровь. Укус наносит губительные повреждения. Чтобы провести атаку укусом, вампир должен сначала провести клинч, захват или бросок (см. ниже). Если один из этих манёвров увенчался успехом, то на следующий ход персонаж может атаковать того же противника укусом. При желании вампир может вместо атаки укусом подарить Поцелуй. В данном случае действуют те же модификаторы манёвра, но он не наносит урона, а жертва в большинстве случаев не имеет возможности ему противостоять (см. стр. 288). Подарив Поцелуй, вампир при желании может бесследно затворить оставленные клыками раны, просто прикоснувшись к ним языком.",
    "численное превосходство": "Персонаж, которому в ближнем бою приходится сражаться с превосходящим численностью противником, получает +1 к сложности проверок атаки и защиты за каждого противника после первого (но не более +4).",
    # 'бросок': "СИЛА + ДРАКА, ТОЧНОСТЬ +0, СЛОЖНОСТЬ +1, УРОН СИЛА+1(С)",
    # 'захват': "СИЛА + ДРАКА, ТОЧНОСТЬ +0, СЛОЖНОСТЬ +0, УРОН НЕТ(П)",
    # 'клинч': "СИЛА + ДРАКА, ТОЧНОСТЬ +0, СЛОЖНОСТЬ +0, УРОН СИЛА(П)"

}

rang_man = {
    'беглый огонь': "Персонаж со скорострельным оружием может выстрелить несколько раз за ход. Для этого он должен разбить свой пул проверки стрельбы на нужное количество выстрелов и выбрать равное количество целей (множественные атаки против одной цели обыгрываются по правилам длинной или короткой очереди). Количество выстрелов не может превышать показателя скорострельности оружия. Каждый выстрел считается отдельной проверкой атаки.",
    'дистанция': "В таблице дистанционного оружия на стр. 301, в графе «Дистанция», указана эффективная дистанция стрельбы из каждого вида оружия; если цель находится в пределах этой дистанции, базовая сложность проверки атаки против неё равна 6. Максимальная дистанция вдвое больше эффективной; если цель находится дальше эффективной, но ближе максимальной дистанции, базовая сложность проверки атаки против неё возрастает до 8. Выстрел в цель, находящуюся в пределах двух метров от стрелка, считается выстрелом в упор; базовая сложность проверки атаки при выстреле в упор равна 4.",
    'длинная очередь': "Персонаж выпускает в цель весь магазин. При этом он проходит одну проверку атаки, но её пул увеличивается на десять d10, а сложность возрастает на два пункта из‑за сильной отдачи. Дополнительные успехи увеличивают пул проверки урона, как если бы это был простой одиночный выстрел. Персонаж, который ведёт огонь длинными очередями, не может целиться в определённую часть тела жертвы. Персонаж может выпустить длинную очередь, только если магазин его оружия полон хотя бы наполовину.",
    'короткая очередь': "Персонаж тратит три патрона за одну атаку, но взамен увеличивает пул проверки атаки на два d10. Не все виды оружия имеют такой режим стрельбы (см. таблицу дистанционного оружия на стр. 301). Сложность проверки атаки возрастает на один пункт из‑за отдачи. Дополнительные успехи увеличивают пул проверки урона, как если бы это был простой одиночный выстрел.",
    'наведение': "Персонаж проводит целый ход, тщательно наводя оружие на цель. Каждый манёвр наведения увеличивает пул проверки последующего одиночного выстрела на один d10. Обратите внимание, что количество этих дополнительных d10 не может превышать показателя восприятия персонажа, а сам персонаж должен обладать навыком стрельбы не ниже 1. Если оружие оснащено оптическим прицелом, то первый манёвр наведения увеличивает пул проверки не на один d10, а сразу на три. Персонаж, который наводит оружие на цель, не может предпринимать других действий. Персонаж не может наводиться на цель, которая движется быстрее, чем шагом",
    'обстрел': "Вместо того чтобы стремиться поразить одну-единственную цель, персонаж, вооружённый автоматическим оружием, может опустошить магазин, обстреляв область диаметром до трёх метров. При этом он проходит одну проверку атаки, но её пул увеличивается на десять d10, а сложность возрастает на два пункта из‑за сильной отдачи. Затем персонаж прибавляет полученные успехи к пулу проверки урона от оружия и разбивает этот пул между всеми целями, оказавшимися в зоне обстрела. Каждая цель должна получить хотя бы по одному d10 — остальные персонаж волен распределять по своему усмотрению. Если в зоне обстрела находится только одна цель, ей достаётся только половина пула — остальные d10 уйдут «в молоко». Если целей больше, чем d10 в пуле проверки урона, значит, ни одна из этих целей не сможет получить более одного d10. Персонаж может предпринять этот манёвр, только если магазин его оружия полон хотя бы наполовину. Сложность проверок уклонения от обстрела увеличивается на один пункт.",
    'перезарядка': "Перезарядка занимает один ход и требует полного внимания персонажа. Как и любой другой манёвр, перезарядка может быть одним из множественных действий.",
    'стрельба по-македонски': "Стрельба с двух рук одновременно считается множественным действием, поэтому персонаж должен распределить пул проверки стрельбы между двумя атаками по своему усмотрению. Кроме того, сложность проверки атаки оружием в неосновной руке возрастает на один пункт (если, конечно, персонаж не амбидекстр). В остальном обе проверки атаки проходят как обычно. Если персонаж атакует одну цель, то разумнее будет использовать правила длинной или короткой очереди.",
    'укрытие': "Укрытие затрудняет попадание по противнику, но иногда мешает и самому противнику вести ответный огонь. Модификаторы сложности атаки для различных укрытий приведены в таблице ниже. Персонаж, который находится в укрытии, также может испытывать неудобства, поскольку для того, чтобы выстрелить в противника, ему нужно сначала высунуться из‑за укрытия, а потом нырнуть обратно. Таким образом, сложность проверок атаки для персонажей, находящихся в укрытии, также возрастает, но этот модификатор будет на один пункт ниже, чем у того, кто пытается его атаковать (если модификатор укрытия равен +1, то персонаж, который находится в этом укрытии, не получит модификатора вовсе). Например, если персонаж спрячется за стеной, то противник получит +2 к сложности проверок атак, проводимых по персонажу, а сам персонаж при этом получит +1 к сложности проверок атаки, проводимой по своему противнику. Обратите внимание, что модификаторы укрытия работают в обе стороны и суммируются, если оба противника находятся в укрытиях. Например, если один персонаж лежит на земле, а другой спрятался за стеной, то оба они получат по +2 к сложности проверок атаки друг по другу.",
}